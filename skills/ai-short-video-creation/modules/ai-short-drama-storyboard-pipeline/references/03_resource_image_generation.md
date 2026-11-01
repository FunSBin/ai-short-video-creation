# Resource Image Prompts And Generation

Use this module when writing resource image prompts or generating resource images.

## General Rules

- One image per resource prompt.
- Do not combine unrelated resources in one image.
- Use the exact filename and reference name from the resource plan.
- Save images to `output/assets/core_resource_images/` unless the project has a different canonical resource folder.
- After generation, inspect for identity, costume, staging, and tradition accuracy.

## Character Resource Prompt Pattern

Default character assets follow [人物图默认交付](../../ai-short-video-assets/references/design-assets.md#人物图默认交付): one pure-white horizontal four-panel board per character, with front full body, exact side full body, back full body and face close-up. A portrait alone is casting input, not the completed asset. Keep the same specification in minimal tests unless the user explicitly changes it.

```text
Create a horizontal live-action character reference board for [角色] on a pure white background.
Exactly four panels, left to right: front full body, strict 90-degree side full body, back full body, and face close-up.
In the first three panels show the complete head-to-shoes figure, neutral stance, at consistent scale.
Keep the same face, age, hair, costume, and body proportions across all views.
Clean even soft lighting, realistic fabric and skin, no scene background.
No text, watermark, logo, subtitles, modern objects, anime, game CG, plastic skin.
```

## Scene Resource Prompt Pattern

Scenes should be reusable cinematic background references:

Repeated locations, area changes and shot/reverse-shot follow [scene coverage](../../ai-short-video-assets/references/scene-coverage.md). Generate a planned area/view, not one local composition for every event. Derive required reverse views from the same approved layout, save them independently, and verify architecture, entrances and lighting. Do not mirror a forward view or invent unseen real-location geometry. Single fixed shots need no unused view set.

```text
Create a horizontal cinematic environment reference for [场景].
Target area: [剧情区域]; viewpoint from [固定地标位置] toward [朝向／对象].
Visible background landmarks: [该方向实际地标]; preserve [同场已锁建筑、通道与光源关系].
Show clear spatial layout, foreground, midground, background, camera direction, entrances and exits.
Prefer empty location unless scale requires crowds or army.
No main characters unless the scene asset is explicitly a crowd or army setup.
No text, watermark, logo, subtitles, modern objects, anime, game CG.
```

## Prop Resource Prompt Pattern

Props should be clean reference images:

```text
Create a clean prop reference image for [道具].
Neutral background, clear silhouette, material, scale, front and side view if useful.
No hands unless hand scale is explicitly needed.
No text, watermark, logo, subtitles, modern objects, anime, game CG.
```

## Monster And Effect Rules

- Match the local religious or mythic iconography.
- Avoid western fantasy monsters unless the tradition calls for them.
- For divine effects, create reference mood and motion logic, not unreadable explosions.

## QA Checklist

- File saved with planned filename.
- No text or labels inside the image.
- Character stage not mixed with another stage.
- Character board has the white background, three complete correctly oriented body views and a clear face close-up, all the same identity and costume; a portrait is not marked as the completed character asset.
- Scene is the intended before or after state.
- Scene actually covers its planned area/direction; paired views agree with one layout. Record unknown or missing backgrounds rather than approving by filename.
- Prop includes all necessary parts such as sword and sheath.
- Traditional creature anatomy is correct.
