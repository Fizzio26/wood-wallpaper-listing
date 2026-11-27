# COSMO 语义框架

## 资料摘要

COSMO（Common Sense Knowledge Generation and Serving System）研究从大规模电商用户行为中挖掘以用户为中心的常识关系，用于丰富商品知识表示。论文描述了候选知识生成、质量过滤与人工标注、知识完善，以及搜索相关性、会话推荐和搜索导航等应用。培训材料对用户意图、Rufus 问答和场景化商品内容的商业化解释，只能作为规划框架，不能当作 Amazon 排名或转化机制的证据。

## Listing 应用方法

从可验证的产品特征出发，依次分析：

1. 该特征是什么，证据来自哪里？
2. 买家拥有该特征时可以完成什么任务？
3. 买家在哪种具体场景需要它？
4. 它解决什么顾虑，如何影响购买选择？
5. 如何用清楚、准确的英语表达，不扩大性能边界？

建议映射结构：产品属性 → 买家任务/意图 → 使用场景 → 解决的问题 → 可验证文案。

## 关系类型参考

培训图片和 XLSX 场景表包含 USE_FOR_FUNC、USE_FOR_EVE、USE_FOR_AUD、CAPABLE_OF、USE_TO、USE_AS、IS_A、USE_ON、USE_IN_LOC、USE_WITH、USE_BY、INTERESTED_IN、X_WANT 等关系。用作构思分类，不应将其误称为 Amazon 官方 Listing 字段。

## COSMO/Rufus 问题覆盖层

Use this layer during planning, after SKU facts are verified and before drafting. It improves answerability and clarity; it does not predict ranking, recommendation, traffic, or conversion.

1. Start from a verified SKU attribute, not a keyword alone.
2. Select only relevant relations. For this category, common choices are `IS_A`, `USE_FOR_FUNC`, `USE_AS`, `CAPABLE_OF`, `USE_IN_LOC`, `USE_WITH`, `USED_BY`, and `X_WANT`.
3. Generate candidate buyer questions in ordinary language. Cover product identity, size/coverage, appearance, fit surfaces, installation, care, removal, and known limitations.
4. Label every answer as **verified**, **needs confirmation**, or **not answerable from Listing facts**. Only verified answers may enter Listing copy. A question can reveal a missing fact, but cannot create a claim.
5. Allocate each retained answer to one field. Prefer the title for product identity, Highlights/Bullets for decision-critical facts, and Description for method, care, and limitations. Avoid repeating the same answer in several fields.

Rufus is an Amazon shopping assistant that can use catalog content, reviews, Q&As, and other information to respond to shopping questions. This supports writing a clear, internally consistent fact set, but does not authorize claims based on reviews, competitor information, or web sources. Do not claim that a Listing is "Rufus optimized" or that it will be surfaced by Rufus.

### Review questions for wood contact paper

- What is it, and what visual result does it offer? (`IS_A`, `USE_AS`)
- What size or coverage does one roll provide? (`IS_A`)
- Which prepared surfaces can use it, and which cannot? (`USE_IN_LOC`)
- How is it measured, cut, and applied? (`USE_FOR_FUNC`)
- What do waterproof and removable mean for this SKU, including limits? (`CAPABLE_OF`)
- What material, texture, coverage, or care question remains unverified? Mark it for confirmation instead of drafting an answer.

Do not use audience, event, room, or accessory relations merely to increase keyword count. Include a scenario only when it has a direct fit with the verified surface and product use.

## 木纹墙纸示例

- Self-adhesive → 希望免用额外胶水完成表面更新 → 平整、清洁、干燥的适用表面 → peel-and-stick application。需核验基材与安装条件。
- Grid backing → 希望测量裁切更方便 → DIY 覆盖柜门、抽屉等 → grid backing helps guide measuring and cutting。须核实该 SKU 确有网格底纸。
- Wood grain appearance → 希望更新表面视觉效果 → 家具、柜门、书架等 → wood-look finish。不得暗示实木材质。
- Waterproof → 担心偶尔水溅 → 适合范围按产品证据描述。用户设定产品防水已验证，但不能扩张为可浸泡、淋浴区适用等未确认用途。

## 质量检查

过滤不完整、与产品无关、没有新信息、不合理或不典型的意图解释。避免把相关性推断写成确定事实。COSMO 资料支持的是以意图和常识丰富商品理解的研究方向，不证明某种文案结构会自动提升排名或流量。
