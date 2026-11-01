# Resource Planning And Naming

Use this module before generating character, scene, prop, monster, or effect images.

For repeated locations, multiple areas, shot/reverse-shot or repetitive backgrounds, read [scene coverage](../../ai-short-video-assets/references/scene-coverage.md). Before batch image generation, map script events to layout, required areas and camera directions; reuse approved coverage and list missing views. A local scene image covers only what it actually shows.

## Resource Categories

- `CHAR_`: human or deity character sheets.
- `SCENE_`: reusable locations and camera-angle variants.
- `PROP_`: hand-held or symbolic objects.
- `MONSTER_`: creatures, demons, divine attendants, beasts.
- `FX_`: reusable visual effects such as divine light, mist, river split, ascension glow.
- `STATUE_`: temple statues, icons, altar references when needed.

## Resource Document Requirements

Each entry must include:

```text
编号和文件名：
引用名称：
类别：
用途：
使用集数和片段：
视觉设定：
生图提示词：
禁止项：
质检重点：
返修记录：
```

For qualifying scene entries add: `场景ID／状态｜剧情区域与连接｜机位位置→朝向｜可见背景地标｜覆盖镜号｜对应图片／待补｜正反打配对ID（适用时）｜来源与验收状态`.

## Planning Rules

- Plan reusable core assets first, then episode-specific supplemental assets.
- Character images should lock identity and costume stages before storyboard generation, using the default pure-white front/side/back full-body plus face close-up board in [人物图默认交付](../../ai-short-video-assets/references/design-assets.md#人物图默认交付). Do not reduce this to a portrait for a minimal test.
- Scene images should usually be empty locations. Add crowds, army, or ritual groups only when the scene itself requires scale.
- Important location variants should be planned by camera logic:
  - protagonist view
  - pursuer or parent view
  - side view for blocking
  - close ground or prop interaction view
  - before-event and after-event variants
- For folklore or iconography, prevent wrong visual traditions in the forbidden list.

## Naming Examples

```text
CHAR_01_真武太子_四视图.png
CHAR_02_真武白衣修道人_四视图.png
SCENE_16_剑河断亲地_斩河前连续干地_空场.png
SCENE_18_剑河两岸_斩河后空场.png
PROP_03_断裂衣角.png
MONSTER_01_龟蛇作乱形态.png
FX_01_五龙捧圣视觉参考.png
```

## Asset Binding Names

Use stable human-readable binding names in video prompts:

```text
真武_太子
真武_白衣修道人
善胜皇后
净乐国王
斩河前连续干地
剑河两岸_斩河后
断裂衣角
黑色长剑
```
