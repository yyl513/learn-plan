/*
 * GitHub 学习提醒 - AutoX.js 定时任务
 * 
 * 使用说明：
 * 1. 将此脚本复制到你的 AutoX.js App 中
 * 2. 设置定时任务（周一、周四 20:00 执行）
 * 3. 脚本会自动打开浏览器带你学习 GitHub
 * 
 * 作者：WorkBuddy AI
 * 创建日期：2026-04-25
 */

// ==================== 配置区域 ====================
const CONFIG = {
    // GitHub 学习资源（可自行修改为当前学习进度对应的页面）
    githubUrl: "https://github.com/skills",
    
    // 学习主题名称
    topic: "GitHub / Git 版本控制",
    
    // 每日任务列表
    tasks: [
        "复习 Git 基本命令（add/commit/push/pull）",
        "实践分支创建与合并",
        "尝试在 GitHub 上参与一个开源项目"
    ],
    
    // 推荐学习资源
    resources: [
        "GitHub Skills: github.com/skills",
        "廖雪峰 Git 教程: liaoxuefeng.com/wiki/git"
    ]
};

// ==================== 主程序 ====================
function main() {
    // 1. 显示欢迎提示
    toast("📚 GitHub 学习提醒");
    sleep(1000);
    
    // 2. 显示今日任务
    showTaskDialog();
    
    // 3. 询问是否开始学习
    let choice = dialogs.confirm(
        "📚 GitHub 学习提醒",
        "今日学习主题：" + CONFIG.topic + "\n\n" +
        "⏰ 学习时长：30分钟\n" +
        "💡 重点：动手实践，不要只看不练！\n\n" +
        "是否打开 GitHub 开始学习？"
    );
    
    if (choice) {
        // 打开 GitHub 学习页面
        openGitHubLearning();
    } else {
        toast("学习计划已记录，稍后记得学习哦~");
    }
}

// 显示今日任务对话框
function showTaskDialog() {
    let taskList = CONFIG.tasks.map((task, i) => 
        (i + 1) + ". " + task
    ).join("\n");
    
    alert(
        "📋 今日 GitHub 学习任务",
        taskList
    );
}

// 打开 GitHub 学习页面
function openGitHubLearning() {
    toast("正在打开 GitHub...");
    
    // 方法1：使用系统浏览器
    app.startActivity({
        action: "android.intent.action.VIEW",
        data: "https://github.com"
    });
    
    sleep(2000);
    
    // 显示学习提示
    toast("💡 先从创建第一个仓库开始吧！");
}

// 显示学习资源
function showResources() {
    let resourceList = CONFIG.resources.join("\n");
    alert("📚 推荐学习资源", resourceList);
}

// ==================== 快捷命令 ====================

// 快速复习 Git 命令
function quickGitReview() {
    alert(
        "🐙 Git 常用命令速查",
        
        "【日常工作流】\n" +
        "git status          - 查看当前状态\n" +
        "git add .           - 添加所有更改\n" +
        "git commit -m 'msg' - 提交更改\n" +
        "git push            - 推送到远程\n\n" +
        
        "【分支操作】\n" +
        "git branch          - 查看分支\n" +
        "git checkout -b xxx - 创建并切换\n" +
        "git merge xxx       - 合并分支\n\n" +
        
        "【其他常用】\n" +
        "git pull            - 拉取更新\n" +
        "git log             - 查看提交历史\n" +
        "git diff            - 查看更改"
    );
}

// ==================== 定时任务入口 ====================
// 设置定时任务时，调用 main() 函数即可

// main();  // 取消注释以启用自动执行

// ==================== 日志记录 ====================
console.show();
print("========== GitHub 学习提醒 ==========");
print("时间：" + new Date().toLocaleString());
print("主题：" + CONFIG.topic);
print("=====================================");
