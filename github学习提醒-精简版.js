/*
 * GitHub 学习提醒 - 精简版（手机专用）
 * 
 * 使用方法：
 * 1. 复制此脚本到 AutoX.js
 * 2. 在 AutoX.js 中设置定时任务（周一、周四 20:00）
 * 3. 运行即可
 */

// GitHub 学习主题
const TOPIC = "GitHub / Git";
const TASKS = [
    "复习 git add/commit/push/pull",
    "练习分支创建与合并",
    "参与开源项目或完善自己的仓库"
];

// 主函数
function startLearning() {
    // 显示任务列表
    let taskText = TASKS.map((t, i) => (i+1) + ". " + t).join("\n");
    
    if (dialogs.confirm("📚 " + TOPIC + " 学习提醒", 
        "今日任务：\n" + taskText + 
        "\n\n⏰ 时长：30分钟\n💡 多动手，别只看！\n\n打开 GitHub 开始学习？")) {
        
        // 打开浏览器
        app.startActivity({
            action: "android.intent.action.VIEW",
            data: "https://github.com"
        });
        
        toast("加油！💪");
    } else {
        toast("稍后记得学习哦~");
    }
}

// 运行
startLearning();
