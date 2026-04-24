#!/usr/bin/env python3
"""
GitHub Actions 学习提醒推送脚本
通过 PushPlus 发送微信提醒
"""

import os
import requests
from datetime import datetime

# 从环境变量获取配置
PUSHPLUS_TOKEN = os.environ.get("PUSHPLUS_TOKEN")
TOPIC = os.environ.get("TOPIC", "github")
TITLE = os.environ.get("TITLE", "学习提醒")
PUSHPLUS_URL = "https://www.pushplus.plus/send"

# 学习提醒内容配置
REMINDERS = {
    "github": {
        "title": "📚 GitHub / Git 版本控制",
        "content": """
        <h2>🎯 今日学习主题</h2>
        <p><strong>GitHub / Git 版本控制</strong></p>
        
        <h3>📋 今日任务</h3>
        <ol>
            <li>复习 Git 基本命令（add/commit/push/pull）</li>
            <li>实践分支创建与合并</li>
            <li>尝试在 GitHub 上参与一个开源项目</li>
        </ol>
        
        <h3>📚 推荐资源</h3>
        <ul>
            <li>GitHub Skills: <a href="https://github.com/skills">github.com/skills</a></li>
            <li>廖雪峰 Git 教程: <a href="https://liaoxuefeng.com/wiki/git">liaoxuefeng.com/wiki/git</a></li>
        </ul>
        
        <p>⏰ <strong>学习时长：30分钟</strong></p>
        <p>💡 <em>重点：动手实践，不要只看不练！</em></p>
        """
    },
    "python": {
        "title": "💻 Python + VSCode 学习",
        "content": """
        <h2>🎯 今日学习主题</h2>
        <p><strong>Python + VSCode 编程</strong></p>
        
        <h3>📋 今日任务</h3>
        <ol>
            <li>打开 VSCode 编写代码</li>
            <li>复习本周学习的 Python 语法点</li>
            <li>完成一个小练习或实战项目</li>
        </ol>
        
        <h3>📚 推荐资源</h3>
        <ul>
            <li>菜鸟教程 Python: <a href="https://runoob.com/python3">runoob.com/python3</a></li>
            <li>VSCode Python 文档: <a href="https://code.visualstudio.com/docs/python/python-tutorial">VSCode 官方教程</a></li>
        </ul>
        
        <p>⏰ <strong>学习时长：30分钟</strong></p>
        <p>💡 <em>重点：多写代码，看十遍不如敲一遍！</em></p>
        """
    },
    "english": {
        "title": "🌐 英语学习",
        "content": """
        <h2>🎯 今日学习主题</h2>
        <p><strong>英语 - 词汇 + 语法 + 听力</strong></p>
        
        <h3>📋 今日任务（30分钟分配）</h3>
        <ol>
            <li>[10分钟] Anki/墨墨背单词复习</li>
            <li>[15分钟] 语法学习或技术文档阅读</li>
            <li>[5分钟] TED 听力或跟读练习</li>
        </ol>
        
        <h3>📚 推荐资源</h3>
        <ul>
            <li>Anki 单词卡组（间隔重复记忆）</li>
            <li>English Grammar in Use</li>
            <li>每日英语听力 App / TED Talks</li>
        </ul>
        
        <p>💡 <em>坚持每天背单词，间隔重复是关键！</em></p>
        """
    },
    "review": {
        "title": "📊 周末学习复盘",
        "content": """
        <h2>📊 本周学习总结</h2>
        
        <p>请回顾本周三个领域的学习情况：</p>
        
        <h3>1️⃣ GitHub</h3>
        <p>学到了什么新知识？有哪些实践？</p>
        
        <h3>2️⃣ Python</h3>
        <p>写了哪些代码？解决了什么问题？</p>
        
        <h3>3️⃣ 英语</h3>
        <p>背了多少新单词？听了什么内容？</p>
        
        <hr/>
        
        <h3>💡 下周改进计划</h3>
        <ul>
            <li>记录本周遇到的问题</li>
            <li>设定下周学习目标</li>
        </ul>
        
        <p>📝 建议：用 Notion 或 GitHub 仓库记录学习日志</p>
        """
    }
}


def send_pushplus(title: str, content: str) -> bool:
    """发送 PushPlus 微信推送"""
    if not PUSHPLUS_TOKEN:
        print("❌ 错误：未设置 PUSHPLUS_TOKEN 环境变量")
        return False
    
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": title,
        "content": content,
        "template": "html"
    }
    
    try:
        response = requests.post(PUSHPLUS_URL, data=data, timeout=10)
        result = response.json()
        
        if result.get("code") == 200:
            print(f"✅ 推送成功！")
            print(f"📅 时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"📌 主题：{title}")
            return True
        else:
            print(f"❌ 推送失败：{result.get('msg', '未知错误')}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误：{e}")
        return False


def main():
    print("=" * 40)
    print("📚 学习提醒推送任务")
    print(f"📅 执行时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)
    
    # 获取今日主题的提醒内容
    reminder = REMINDERS.get(TOPIC, REMINDERS["github"])
    
    # 发送推送
    success = send_pushplus(reminder["title"], reminder["content"])
    
    if success:
        print("\n✨ 今日学习提醒已送达！")
    else:
        print("\n⚠️ 推送失败，请检查配置")
        exit(1)


if __name__ == "__main__":
    main()
