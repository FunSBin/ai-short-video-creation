---
name: ai-short-drama-storyboard-pipeline
description: Use when the user is creating AI short-drama episodes and needs a guided workflow from story outline, resources, storyboard script and images, direct-input director cards, continuous action or continuous combat, through Seedance 2.0 prompts and downloaded video review. Trigger for Chinese requests mentioning 短剧创作, 资源图, 分镜脚本, 黑白多宫格, 导演卡, 连续打斗, Seedance, 全图参考, 视频提示词, 成片复盘, or 下载视频分析.
metadata:
  short-description: AI短剧从剧本到资源图、分镜图、视频提示词流水线
---

# AI Short-Drama Storyboard Video Pipeline

Use this skill as the director pipeline for myth, folk-belief, historical, fantasy, or cinematic AI short-drama projects. Keep continuity, resources, storyboard images, and video prompts synchronized.

For video configuration, use [project settings and execution permissions](../ai-short-video-seedance/references/generation-defaults.md). Historical model examples do not prove current capabilities or authorize submissions.

## Core Principle

Do not treat script, assets, storyboard, and video prompts as separate writing tasks. Each downstream document must inherit and verify upstream decisions:

```text
outline and research
-> script
-> resource plan and resource image prompts
-> generated resource images and QA
-> storyboard script
-> black-and-white multi-panel storyboard prompts
-> generated multi-panel storyboard boards and QA
-> direct-input director cards for continuous action
-> Seedance 2.0 full-reference video prompts
-> downloaded video review, test feedback, and document backfill
```

## When Starting A Project Or Episode

1. Inspect existing project files before drafting.
2. Identify the current stage: outline, script, resources, storyboard, storyboard images, Seedance prompts, or test feedback.
3. If myth or folklore accuracy matters, use research-grounded facts already present in the project, or browse credible sources when facts are uncertain or could be wrong.
4. Work in local Markdown documents. Prefer stable filenames with episode prefixes such as `E01_`.
5. Before generating images, create or update the relevant prompt document and asset list.
6. After generating or revising images, update the downstream docs so later prompts reference the current canonical files.

## Reference Modules

Read only the reference needed for the current stage:

- Story outline to script: `references/01_story_to_script.md`
- Resource planning and naming: `references/02_resource_planning.md`
- Resource image prompts and generation: `references/03_resource_image_generation.md`
- Storyboard script: `references/04_storyboard_script.md`
- Black-and-white multi-panel storyboard images: `references/05_bw_multi_panel_storyboards.md`
- Seedance 2.0 full-reference prompts: `references/06_seedance2_prompts.md`
- Continuity, staging, lip-sync, and QA: `references/07_validation_and_feedback.md`
- Continuous-action direct-input director cards: `references/08_continuous_action_director_cards.md`
- Repeated locations, multiple areas, shot/reverse-shot or repetitive backgrounds: [scene coverage](../ai-short-video-assets/references/scene-coverage.md). Carry its coverage table, paired views and shot-to-image mapping through resources, boards and video prompts; keep this shared standard instead of a separate scene rule set.

## Templates

Use these templates when creating new documents:

- `templates/resource_prompt_doc_template.md`
- `templates/storyboard_script_template.md`
- `templates/bw_multi_panel_prompt_template.md`
- `templates/seedance2_prompt_template.md`
- `templates/continuous_action_director_card_template.md`

## Required Pipeline Documents

For each project, maintain these document families when relevant:

- Resource plan and prompts: `output/*资源图*提示词*.md`
- Character and scene setup for video platforms: `output/*角色基础形象*场景*.md`
- Episode storyboard script: `output/E##_分镜脚本*.md`
- Multi-panel storyboard prompt doc: `output/E##_黑白多宫格分镜提示词*.md`
- Seedance prompts: `output/E##_seedance2_全图参考提示词*.md`

## Image Generation Rules

When the user asks to generate images directly:

- Use the local image generation capability or the project’s chosen image tool.
- Generate one target image per prompt unless the prompt explicitly asks for a multi-panel storyboard board.
- Save outputs into stable folders such as:
  - `output/assets/core_resource_images/`
  - `output/assets/E##_storyboard_boards/`
- Do not overwrite canonical images without user intent. Save revised versions or archive stale versions.
- After generation, visually inspect images when possible and update prompt docs with correction notes.
- For combat or tightly connected motion, inspect the director-card bitmap row by row before binding it as the primary motion reference.

## Director QA Rules

Before finalizing any storyboard or Seedance prompt, check:

- Continuity: no object or event reappears after being removed, destroyed, or transformed.
- Time logic: do not show effects before the triggering action.
- Staging: define camera side, who faces camera, who is back or side-back to camera, foreground, midground, background.
- Scene coverage: map each used area and camera direction to the actual scene image. Prepare missing reverse backgrounds for planned shot/reverse-shot; check repeated local backgrounds across adjacent shots, retaining deliberate fixed compositions.
- Asset binding: every person, scene, prop, monster, or effect mentioned in action text must appear in the reference list.
- Dialogue: visible speakers must have natural lip sync; off-screen lines must be marked as voice-over or off-screen audio.
- Duration: determine seconds from the current scene and verified endpoint, preserving dialogue and action logic. Use the current project model and verified endpoint; apply historical model limits only when that model is selected and the limit remains verified.
- Black-and-white storyboards are director boards, not final art. Prioritize staging, camera, action, and labels over beauty.
- Continuous action: do not turn one fight into independent static target poses; preserve previous-clip force and cut to the next clip during motion.
- Versioning: archive stale cards with a failure reason and keep one canonical current card in the production directory.
