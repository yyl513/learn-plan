#!/usr/bin/env python3
"""
PushPlus 微信推送脚本
用于发送学习提醒到微信
"""

import requests
import json
import sys
from datetime import datetime

# PushPlus 配置
PUSHPLUS_TOKEN = "de4b71e6865346a79c154dcef366b377"
PUSHPLUS_URL = "https://www.pushplus.plus/send"


def send_message(title: str, content: str) -> bool:
    """
    发送微信推送消息
    
    Args:
        title: 消息标题
        content: 消息内容（支持 HTML）
    
    Returns:
        bool: 是否发送成功
    """
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": title,
        "content": content,
        "template": "html"  # 支持 html/markdown/plain 类型
    }
    
    try:
        response = requests.post(PUSHPLUS_URL, data=data, timeout=10)
        result = response.json()
        
        if result.get("code") == 200:
            print(f"✅ 推送成功！")
            return True
        else:
            print(f"❌ 推送失败：{result.get('msg', '未知错误')}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误：{e}")
        return False


def send_learning_reminder(topic: str, content: str):
    """发送学习提醒"""
    title = f"📚 {topic} - 学习提醒"
    html_content = f"""
    <h2>{topic}</h2>
    <hr/>
    {content}
    <hr/>
    <p style="color: #666;">⏰ 提醒时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    """
    send_message(title, html_content)


# 预定义的学习提醒消息
REMINDERS = {
    "github": {
        "title": "GitHub / Git 版本控制",
        "content": """
        <b>📋 今日学习内容：</b>
        <ul>
            <li>复习 Git 基本命令（add/commit/push/pull）</li>
            <li>实践分支创建与合并</li>
            <li>尝试在 GitHub 上参与一个开源项目</li>
        </ul>
        <b>📚 推荐资源：</b>
        <ul>
            <li>GitHub Skills: github.com/skills</li>
            <li>廖雪峰 Git 教程</li>
        </ul>
        <p>⏰ 学习时长：30分钟</p>
        """
    },
    "python": {
        "title": "Python + VSCode",
        "content": """
        <b>📋 今日学习内容：</b>
        <ul>
            <li>打开 VSCode 编写代码</li>
            <li>复习本周学习的 Python 语法点</li>
            <li>完成一个小练习或实战项目</li>
        </ul>
        <b>📚 推荐资源：</b>
        <ul>
            <li>菜鸟教程 Python: runoob.com/python3</li>
            <li>VSCode Python 官方文档</li>
        </ul>
        <p>⏰ 学习时长：30分钟</p>
        <p>💡 重点：多写代码，看十遍不如敲一遍！</p>
        """
    },
    "english": {
        "title": "英语学习",
        "content": """
        <b>📋 今日学习内容（30分钟分配）：</b>
        <ol>
            <li>[10分钟] Anki/墨墨背单词复习</li>
            <li>[15分钟] 语法学习或技术文档阅读</li>
            <li>[5分钟] TED 听力或跟读练习</li>
        </ol>
        <b>📚 推荐资源：</b>
        <ul>
            <li>Anki 单词卡组</li>
            <li>English Grammar in Use</li>
            <li>每日英语听力 App</li>
        </ul>
        <p>💡 坚持每天背单词，间隔重复是关键！</p>
        """
    },
    "review": {
        "title": "周末学习复盘",
        "content": """
        <h3>📊 本周学习总结</h3>
        <p>请回顾本周三个领域的学习情况：</p>
        <ol>
            <li><b>GitHub</b>：学到了什么新知识？</li>
            <li><b>Python</b>：写了哪些代码？</li>
            <li><b>英语</b>：背了多少新单词？</li>
        </ol>
        <h3>💡 下周改进计划</h3>
        <ul>
            <li>记录本周遇到的问题</li>
            <li>设定下周学习目标</li>
        </ul>
        """
    }
}


def main():
    if len(sys.argv) < 2:
        print("用法: python3 pushplus.py <topic>")
        print("可用 topic:")
        for key in REMINDERS:
            print(f"  - {key}")
        sys.exit(1)
    
    topic = sys.argv[1]
    
    if topic not in REMINDERS:
        print(f"❌ 未知 topic: {topic}")
        print(f"可用 topic: {', '.join(REMINDERS.keys())}")
        sys.exit(1)
    
    reminder = REMINDERS[topic]
    send_learning_reminder(reminder["title"], reminder["content"])


if __name__ == "__main__":
    main()
