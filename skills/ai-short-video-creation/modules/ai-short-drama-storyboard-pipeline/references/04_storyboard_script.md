# Storyboard Script

Use this module when converting a script into a director storyboard script.

## Shot Fields

Each shot should include:

```text
镜头编号：
时长：
剧情功能：
画面内容：
人物站位：
镜头位置：
场景ID／状态／区域：
机位位置→朝向与可见背景地标：
对应纯场景图：
正反打配对镜号（适用时）：
运镜：
对白和口型：
声音：
使用资源：
转场：
风险点：
```

## Shot Design Rules

Repeated locations, multiple areas and shot/reverse-shot follow [scene coverage](../../ai-short-video-assets/references/scene-coverage.md). Use the coverage table to bind each view; missing reverse backgrounds return to assets. Pair shots only when the scene needs both subjects/directions visible; off-screen replies and deliberate fixed shots do not require extra cuts. Compare same-scene backgrounds before batch boards and again after visual generation; changing faces or cropping alone does not establish another area.

- Design shots for video generation and editing, not just still composition.
- Each shot should have one main action. If multiple actions compete, split the shot.
- Mark whether adjacent shots are:
  - hard cut
  - action continuity
  - gaze match
  - prop match
  - light or atmosphere match
- For action scenes, lock the ground relationship before describing effects.
- For emotional scenes, lock who is looking at whom before describing facial expression.

## Continuity Rules

- If a prop leaves a hand in one shot, it cannot be in that hand in the next shot.
- If a river, fire, wound, broken object, divine light, or transformation appears after an action, do not show it before the action.
- If a character exits toward a door or mountain, do not put the destination behind the wrong character in reverse shots.

## Dialogue And Lip-Sync

- Use visible dialogue only when the speaker mouth is visible.
- Use off-screen voice when the camera prioritizes a prop, back view, or wide shot.
- One time segment should usually have one lip-sync owner.
- Add `其他人物不说话，嘴部闭合` when multiple characters are visible.
