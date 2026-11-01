# Seedance 2.0 Full-Reference Prompts

Use this module when turning storyboard boards and resources into Seedance 2.0 or similar full-reference video prompts.

This is a legacy compatibility guide. The user's default is [Seedance 2.5 Draft / 16:9 / 480P preview with content-driven duration](../../ai-short-video-seedance/references/generation-defaults.md). For the default route use the current [Seedance prompt skill](../../ai-short-video-seedance/SKILL.md) and its full template; do not inherit the legacy 15-second cap or reduced section skeleton below. The following Seedance 2.0 examples apply only when that model is explicitly selected.

## Clip Duration

- Seedance 2.0 clips can be up to 15 seconds.
- Do not force every segment to be shorter. Use the full 15 seconds when dialogue or action needs it.
- If a segment still has too many actions, split it into A and B clips.

## Standalone Clip Mode

- Treat each Seedance prompt as an independent clip by default. Describe the opening pose, location, actors, and immediate first action inside the prompt; do not assume the model knows any episode or segment number.
- Use cross-clip continuation language only when the user explicitly supplies a previous video/extension workflow or asks for an action-match continuation. Otherwise, use `standalone prompt` and include `no unexplained previous-clip references` in the review checklist.
- Do not write “承接S08/S09”, “previous clip”, or “continue the last segment” in a standalone prompt. Replace it with a concrete visible start state such as “真武已经处于低位持剑姿态，蛇魔在右侧，龟魔在左侧”。

## Required Sections

Every clip prompt should include:

```text
【基础设定】
【分镜多宫格参考】
【人物站位与镜头方向】
【画面内容】
【声音】
【禁止项】
```

## Basic Setting Rules

`【基础设定】` must list every asset mentioned later in `【画面内容】`:

```text
真武：@引用“真武_白衣修道人”
善胜皇后：@引用“善胜皇后”
黑色长剑：@引用“黑色长剑”
断裂衣角：@引用“断裂衣角”
斩河前连续干地：@引用“斩河前连续干地”
剑河两岸：@引用“剑河两岸_斩河后”
```

Do not mention a person, location, prop, monster, or effect in action text unless it is bound in the basic setting.

## Multi-Panel Reference Rules

- Use the section title `【分镜多宫格参考】`.
- Specify board filename and exact panel range.
- If the clip continues from a previous panel, explicitly mention the previous event state.
- Tell the model that labels, arrows, panel numbers, and Chinese annotations are only for reference and must not appear in video.

## Director-Card-First Binding

For combat, chase, rescue, or transformation, use the approved director card as the primary motion reference. Map each timed block to the matching card row.

When the card includes a top-down / overhead / bird's-eye overview staging diagram, treat it as a spatial map only, not shot 1. Do not ask Seedance to reproduce the overview as the opening video image. Timed video mapping starts from the first action row labeled shot 1, while the overview only locks axis, camera side, screen direction, actor positions, attack lanes, and forbidden reverse placement.
In standalone clip mode, the first timed row must be self-sufficient. Do not tell Seedance to replay, finish, or continue an event that only exists in another clip.

Use character, monster, prop, and effect images as identity and appearance only. Use clean scene images as environment and camera-direction locks. Do not let a composite resource override the card's pose, action, or staging.

If an ordinary storyboard and a director card disagree, fix the documents before generation; do not upload both and ask Seedance to decide.

## Staging Rules

Every clip needs a camera and blocking layer:

```text
空间轴线：
镜头站位：
面对镜头：
背对或侧背对镜头：
前景：
中景：
背景：
严禁错位：
```

Use side face, side-back, or back view when needed. Do not force every character to face the camera.

## Action Rules

- Describe concrete body mechanics: hand, foot, gaze, blade direction, object contact point.
- Effects happen after the triggering action, not before.
- Use one main action per time block.
- Write combat as call-and-response: attacker commits to one move, defender visibly reacts at the contact point, then the attacker or environment follows through. Do not write a list of attacks without the receiving body's reaction.
- Treat one move per clip or one move per time block as the default combat limit. If a beat needs wind-up, impact, and recovery, keep those three stages in the same causal beat instead of adding another attack.
- With three or more active combatants, choose one primary exchange per beat and keep the other threat as readable background pressure. If two active exchanges cannot remain legible, split the clip or reduce the number of simultaneous attackers.
- For sword or weapon actions, specify one weapon only and its direction.
- Keep attacker response, defender mechanics, and the resulting effect in the same shot whenever they form one causal beat.
- Start from the previous clip's unfinished motion. Do not replay that clip's completed move.
- End with an action-match cut or cut during motion; do not spend the remaining duration holding a finished pose.
- Add measurable caps only when they prevent an observed failure, such as full-body interaction share, maximum completed-pose hold, maximum isolated insert, or maximum contact hold.

## Dialogue And Lip-Sync

- Visible speaker: `某某嘴部清晰可见，自然开合对口型，说：“...”`
- Off-screen line: `某某作为画外声，不要求画面中任何人口型`
- Non-speakers: `其他人物不说话，嘴部闭合`
- Do not shorten dialogue until the logic breaks. Increase duration up to 15 seconds or split the clip.

## Seedance Prompt Skeleton

```text
片段时长：__ 秒
上传多宫格分镜板：`__`
参考宫格：第 __ 格
推荐裁切：`__`

【基础设定】
...

【分镜多宫格参考】
...

【连续动作与首尾衔接】
上一片尾动作：
本片首动作：
本片禁止重复：
本片尾动作：
下一片承接：

【人物站位与镜头方向】
...

【画面内容】
0-3秒，...
3-6秒，...

【声音】
...

【禁止项】
...
```
