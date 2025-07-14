{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "db0c8a43-fa3c-4b45-869d-f316165dc0b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import polars as pl\n",
    "from pathlib import Path\n",
    "\n",
    "# CHANGE THIS to the path of your dataset\n",
    "filename = \"2024_fb_ads_president_scored_anon.csv\"\n",
    "\n",
    "# Optional: Define group keys (if you want grouped stats later)\n",
    "group_keys = [\"Page Id\", \"Ad Id\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bf559c09-26d6-461f-939f-51b70bacbdf8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loaded 246745 rows and 41 columns from 2024_fb_ads_president_scored_anon.csv\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><style>\n",
       ".dataframe > thead > tr,\n",
       ".dataframe > tbody > tr {\n",
       "  text-align: right;\n",
       "  white-space: pre-wrap;\n",
       "}\n",
       "</style>\n",
       "<small>shape: (5, 41)</small><table border=\"1\" class=\"dataframe\"><thead><tr><th>page_id</th><th>ad_id</th><th>ad_creation_time</th><th>bylines</th><th>currency</th><th>delivery_by_region</th><th>demographic_distribution</th><th>estimated_audience_size</th><th>estimated_impressions</th><th>estimated_spend</th><th>publisher_platforms</th><th>illuminating_scored_message</th><th>illuminating_mentions</th><th>scam_illuminating</th><th>election_integrity_Truth_illuminating</th><th>advocacy_msg_type_illuminating</th><th>issue_msg_type_illuminating</th><th>attack_msg_type_illuminating</th><th>image_msg_type_illuminating</th><th>cta_msg_type_illuminating</th><th>engagement_cta_subtype_illuminating</th><th>fundraising_cta_subtype_illuminating</th><th>voting_cta_subtype_illuminating</th><th>covid_topic_illuminating</th><th>economy_topic_illuminating</th><th>education_topic_illuminating</th><th>environment_topic_illuminating</th><th>foreign_policy_topic_illuminating</th><th>governance_topic_illuminating</th><th>health_topic_illuminating</th><th>immigration_topic_illuminating</th><th>lgbtq_issues_topic_illuminating</th><th>military_topic_illuminating</th><th>race_and_ethnicity_topic_illuminating</th><th>safety_topic_illuminating</th><th>social_and_cultural_topic_illuminating</th><th>technology_and_privacy_topic_illuminating</th><th>womens_issue_topic_illuminating</th><th>incivility_illuminating</th><th>freefair_illuminating</th><th>fraud_illuminating</th></tr><tr><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>i64</td><td>i64</td><td>i64</td><td>str</td><td>str</td><td>str</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td></tr></thead><tbody><tr><td>&quot;4ff23a48b53d988df50ddfebb0e442…</td><td>&quot;0ddb025b8544e2d58e6977ad417e74…</td><td>&quot;2024-10-21&quot;</td><td>&quot;Texas Organizing Project PAC&quot;</td><td>&quot;USD&quot;</td><td>&quot;{&#x27;Texas&#x27;: {&#x27;spend&#x27;: 249, &#x27;impr…</td><td>&quot;{&#x27;female_18-24&#x27;: {&#x27;spend&#x27;: 28,…</td><td>30000</td><td>47499</td><td>249</td><td>&quot;[&#x27;facebook&#x27;, &#x27;instagram&#x27;]&quot;</td><td>&quot;362d68d42e34e070bc9f999033642b…</td><td>&quot;[&#x27;Kamala Harris&#x27;, &#x27;Tim Walz&#x27;]&quot;</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>&quot;4ff23a48b53d988df50ddfebb0e442…</td><td>&quot;86229868e6bde3661724fe02da9350…</td><td>&quot;2024-10-18&quot;</td><td>&quot;Texas Organizing Project PAC&quot;</td><td>&quot;USD&quot;</td><td>&quot;{&#x27;Texas&#x27;: {&#x27;spend&#x27;: 49, &#x27;impre…</td><td>&quot;{&#x27;female_18-24&#x27;: {&#x27;spend&#x27;: 8, …</td><td>75000</td><td>22499</td><td>49</td><td>&quot;[&#x27;facebook&#x27;, &#x27;instagram&#x27;]&quot;</td><td>&quot;dc522d5aa4f91c326d105ec4c482cf…</td><td>&quot;[&#x27;Kamala Harris&#x27;, &#x27;Tim Walz&#x27;]&quot;</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>&quot;4ff23a48b53d988df50ddfebb0e442…</td><td>&quot;07b5aefc27e872e971f793e49aac38…</td><td>&quot;2024-10-13&quot;</td><td>&quot;Texas Organizing Project PAC&quot;</td><td>&quot;USD&quot;</td><td>&quot;{&#x27;Texas&#x27;: {&#x27;spend&#x27;: 149, &#x27;impr…</td><td>&quot;{&#x27;female_18-24&#x27;: {&#x27;spend&#x27;: 26,…</td><td>75000</td><td>32499</td><td>149</td><td>&quot;[&#x27;facebook&#x27;, &#x27;instagram&#x27;]&quot;</td><td>&quot;6dc61896f4a44cf4fdbe564604bbeb…</td><td>&quot;[&#x27;Kamala Harris&#x27;, &#x27;Tim Walz&#x27;]&quot;</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>&quot;b9eb7e353e596d5fc99568d4ef77d4…</td><td>&quot;c62978153c04116d88ead493799168…</td><td>&quot;2024-11-02&quot;</td><td>null</td><td>&quot;USD&quot;</td><td>&quot;{}&quot;</td><td>&quot;{}&quot;</td><td>1000001</td><td>499</td><td>49</td><td>&quot;[&#x27;facebook&#x27;, &#x27;instagram&#x27;, &#x27;aud…</td><td>&quot;5ffb1d89916e779d01193e726cd880…</td><td>&quot;[&#x27;Tim Walz&#x27;]&quot;</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>&quot;b9eb7e353e596d5fc99568d4ef77d4…</td><td>&quot;785e91ef18a5794565af03a6df4e70…</td><td>&quot;2024-11-02&quot;</td><td>null</td><td>&quot;USD&quot;</td><td>&quot;{}&quot;</td><td>&quot;{}&quot;</td><td>1000001</td><td>499</td><td>49</td><td>&quot;[&#x27;facebook&#x27;, &#x27;instagram&#x27;, &#x27;aud…</td><td>&quot;b7360494f7dd93ffa2320d88b10a58…</td><td>&quot;[&#x27;Tim Walz&#x27;]&quot;</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></tbody></table></div>"
      ],
      "text/plain": [
       "shape: (5, 41)\n",
       "┌───────────┬───────────┬───────────┬───────────┬───┬───────────┬───────────┬───────────┬──────────┐\n",
       "│ page_id   ┆ ad_id     ┆ ad_creati ┆ bylines   ┆ … ┆ womens_is ┆ incivilit ┆ freefair_ ┆ fraud_il │\n",
       "│ ---       ┆ ---       ┆ on_time   ┆ ---       ┆   ┆ sue_topic ┆ y_illumin ┆ illuminat ┆ luminati │\n",
       "│ str       ┆ str       ┆ ---       ┆ str       ┆   ┆ _illumina ┆ ating     ┆ ing       ┆ ng       │\n",
       "│           ┆           ┆ str       ┆           ┆   ┆ tin…      ┆ ---       ┆ ---       ┆ ---      │\n",
       "│           ┆           ┆           ┆           ┆   ┆ ---       ┆ i64       ┆ i64       ┆ i64      │\n",
       "│           ┆           ┆           ┆           ┆   ┆ i64       ┆           ┆           ┆          │\n",
       "╞═══════════╪═══════════╪═══════════╪═══════════╪═══╪═══════════╪═══════════╪═══════════╪══════════╡\n",
       "│ 4ff23a48b ┆ 0ddb025b8 ┆ 2024-10-2 ┆ Texas Org ┆ … ┆ 0         ┆ 0         ┆ 0         ┆ 0        │\n",
       "│ 53d988df5 ┆ 544e2d58e ┆ 1         ┆ anizing   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 0ddfebb0e ┆ 6977ad417 ┆           ┆ Project   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 442…      ┆ e74…      ┆           ┆ PAC       ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 4ff23a48b ┆ 86229868e ┆ 2024-10-1 ┆ Texas Org ┆ … ┆ 0         ┆ 0         ┆ 0         ┆ 0        │\n",
       "│ 53d988df5 ┆ 6bde36617 ┆ 8         ┆ anizing   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 0ddfebb0e ┆ 24fe02da9 ┆           ┆ Project   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 442…      ┆ 350…      ┆           ┆ PAC       ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 4ff23a48b ┆ 07b5aefc2 ┆ 2024-10-1 ┆ Texas Org ┆ … ┆ 0         ┆ 0         ┆ 0         ┆ 0        │\n",
       "│ 53d988df5 ┆ 7e872e971 ┆ 3         ┆ anizing   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 0ddfebb0e ┆ f793e49aa ┆           ┆ Project   ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 442…      ┆ c38…      ┆           ┆ PAC       ┆   ┆           ┆           ┆           ┆          │\n",
       "│ b9eb7e353 ┆ c62978153 ┆ 2024-11-0 ┆ null      ┆ … ┆ 0         ┆ 0         ┆ 0         ┆ 0        │\n",
       "│ e596d5fc9 ┆ c04116d88 ┆ 2         ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 9568d4ef7 ┆ ead493799 ┆           ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 7d4…      ┆ 168…      ┆           ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "│ b9eb7e353 ┆ 785e91ef1 ┆ 2024-11-0 ┆ null      ┆ … ┆ 0         ┆ 0         ┆ 0         ┆ 0        │\n",
       "│ e596d5fc9 ┆ 8a5794565 ┆ 2         ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 9568d4ef7 ┆ af03a6df4 ┆           ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "│ 7d4…      ┆ e70…      ┆           ┆           ┆   ┆           ┆           ┆           ┆          │\n",
       "└───────────┴───────────┴───────────┴───────────┴───┴───────────┴───────────┴───────────┴──────────┘"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check if file exists\n",
    "if not Path(filename).exists():\n",
    "    raise FileNotFoundError(f\"File not found: {filename}\")\n",
    "\n",
    "# Load dataset\n",
    "df = pl.read_csv(filename)\n",
    "print(f\"Loaded {df.shape[0]} rows and {df.shape[1]} columns from {filename}\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a7ac500-4d60-4caf-93a9-44f174c4f218",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Numeric columns: ['estimated_audience_size', 'estimated_impressions', 'estimated_spend', 'scam_illuminating', 'election_integrity_Truth_illuminating', 'advocacy_msg_type_illuminating', 'issue_msg_type_illuminating', 'attack_msg_type_illuminating', 'image_msg_type_illuminating', 'cta_msg_type_illuminating', 'engagement_cta_subtype_illuminating', 'fundraising_cta_subtype_illuminating', 'voting_cta_subtype_illuminating', 'covid_topic_illuminating', 'economy_topic_illuminating', 'education_topic_illuminating', 'environment_topic_illuminating', 'foreign_policy_topic_illuminating', 'governance_topic_illuminating', 'health_topic_illuminating', 'immigration_topic_illuminating', 'lgbtq_issues_topic_illuminating', 'military_topic_illuminating', 'race_and_ethnicity_topic_illuminating', 'safety_topic_illuminating', 'social_and_cultural_topic_illuminating', 'technology_and_privacy_topic_illuminating', 'womens_issue_topic_illuminating', 'incivility_illuminating', 'freefair_illuminating', 'fraud_illuminating']\n",
      "Non-numeric columns: ['page_id', 'ad_id', 'ad_creation_time', 'bylines', 'currency', 'delivery_by_region', 'demographic_distribution', 'publisher_platforms', 'illuminating_scored_message', 'illuminating_mentions']\n"
     ]
    }
   ],
   "source": [
    "numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in [pl.Float64, pl.Int64]]\n",
    "non_numeric_cols = [col for col in df.columns if col not in numeric_cols]\n",
    "\n",
    "print(\"Numeric columns:\", numeric_cols)\n",
    "print(\"Non-numeric columns:\", non_numeric_cols)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d9c9c980-ae70-4ebd-90a2-895548c6c986",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><style>\n",
       ".dataframe > thead > tr,\n",
       ".dataframe > tbody > tr {\n",
       "  text-align: right;\n",
       "  white-space: pre-wrap;\n",
       "}\n",
       "</style>\n",
       "<small>shape: (1, 125)</small><table border=\"1\" class=\"dataframe\"><thead><tr><th>Row Count</th><th>estimated_audience_size | Mean</th><th>estimated_impressions | Mean</th><th>estimated_spend | Mean</th><th>scam_illuminating | Mean</th><th>election_integrity_Truth_illuminating | Mean</th><th>advocacy_msg_type_illuminating | Mean</th><th>issue_msg_type_illuminating | Mean</th><th>attack_msg_type_illuminating | Mean</th><th>image_msg_type_illuminating | Mean</th><th>cta_msg_type_illuminating | Mean</th><th>engagement_cta_subtype_illuminating | Mean</th><th>fundraising_cta_subtype_illuminating | Mean</th><th>voting_cta_subtype_illuminating | Mean</th><th>covid_topic_illuminating | Mean</th><th>economy_topic_illuminating | Mean</th><th>education_topic_illuminating | Mean</th><th>environment_topic_illuminating | Mean</th><th>foreign_policy_topic_illuminating | Mean</th><th>governance_topic_illuminating | Mean</th><th>health_topic_illuminating | Mean</th><th>immigration_topic_illuminating | Mean</th><th>lgbtq_issues_topic_illuminating | Mean</th><th>military_topic_illuminating | Mean</th><th>race_and_ethnicity_topic_illuminating | Mean</th><th>safety_topic_illuminating | Mean</th><th>social_and_cultural_topic_illuminating | Mean</th><th>technology_and_privacy_topic_illuminating | Mean</th><th>womens_issue_topic_illuminating | Mean</th><th>incivility_illuminating | Mean</th><th>freefair_illuminating | Mean</th><th>fraud_illuminating | Mean</th><th>estimated_audience_size | Min</th><th>estimated_impressions | Min</th><th>estimated_spend | Min</th><th>scam_illuminating | Min</th><th>election_integrity_Truth_illuminating | Min</th><th>&hellip;</th><th>social_and_cultural_topic_illuminating | Max</th><th>technology_and_privacy_topic_illuminating | Max</th><th>womens_issue_topic_illuminating | Max</th><th>incivility_illuminating | Max</th><th>freefair_illuminating | Max</th><th>fraud_illuminating | Max</th><th>estimated_audience_size | StdDev</th><th>estimated_impressions | StdDev</th><th>estimated_spend | StdDev</th><th>scam_illuminating | StdDev</th><th>election_integrity_Truth_illuminating | StdDev</th><th>advocacy_msg_type_illuminating | StdDev</th><th>issue_msg_type_illuminating | StdDev</th><th>attack_msg_type_illuminating | StdDev</th><th>image_msg_type_illuminating | StdDev</th><th>cta_msg_type_illuminating | StdDev</th><th>engagement_cta_subtype_illuminating | StdDev</th><th>fundraising_cta_subtype_illuminating | StdDev</th><th>voting_cta_subtype_illuminating | StdDev</th><th>covid_topic_illuminating | StdDev</th><th>economy_topic_illuminating | StdDev</th><th>education_topic_illuminating | StdDev</th><th>environment_topic_illuminating | StdDev</th><th>foreign_policy_topic_illuminating | StdDev</th><th>governance_topic_illuminating | StdDev</th><th>health_topic_illuminating | StdDev</th><th>immigration_topic_illuminating | StdDev</th><th>lgbtq_issues_topic_illuminating | StdDev</th><th>military_topic_illuminating | StdDev</th><th>race_and_ethnicity_topic_illuminating | StdDev</th><th>safety_topic_illuminating | StdDev</th><th>social_and_cultural_topic_illuminating | StdDev</th><th>technology_and_privacy_topic_illuminating | StdDev</th><th>womens_issue_topic_illuminating | StdDev</th><th>incivility_illuminating | StdDev</th><th>freefair_illuminating | StdDev</th><th>fraud_illuminating | StdDev</th></tr><tr><td>u32</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>&hellip;</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>246745</td><td>556462.855969</td><td>45601.525952</td><td>1061.291434</td><td>0.071633</td><td>0.050088</td><td>0.548631</td><td>0.381649</td><td>0.271856</td><td>0.222704</td><td>0.572769</td><td>0.12487</td><td>0.228487</td><td>0.143845</td><td>0.024876</td><td>0.122122</td><td>0.014327</td><td>0.021249</td><td>0.005265</td><td>0.025642</td><td>0.10919</td><td>0.033569</td><td>0.00323</td><td>0.002176</td><td>0.012434</td><td>0.033723</td><td>0.105838</td><td>0.001155</td><td>0.080909</td><td>0.187526</td><td>0.006416</td><td>0.002638</td><td>0</td><td>499</td><td>49</td><td>0</td><td>0</td><td>&hellip;</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>409864.758823</td><td>136790.769901</td><td>4992.560749</td><td>0.257879</td><td>0.218127</td><td>0.49763</td><td>0.485792</td><td>0.444917</td><td>0.416062</td><td>0.494677</td><td>0.330572</td><td>0.419859</td><td>0.350933</td><td>0.155747</td><td>0.327427</td><td>0.118833</td><td>0.144212</td><td>0.072366</td><td>0.158065</td><td>0.311878</td><td>0.180118</td><td>0.056742</td><td>0.046601</td><td>0.110812</td><td>0.180516</td><td>0.307631</td><td>0.033966</td><td>0.272697</td><td>0.390334</td><td>0.07984</td><td>0.051297</td></tr></tbody></table></div>"
      ],
      "text/plain": [
       "shape: (1, 125)\n",
       "┌───────────┬───────────┬───────────┬───────────┬───┬───────────┬───────────┬───────────┬──────────┐\n",
       "│ Row Count ┆ estimated ┆ estimated ┆ estimated ┆ … ┆ womens_is ┆ incivilit ┆ freefair_ ┆ fraud_il │\n",
       "│ ---       ┆ _audience ┆ _impressi ┆ _spend |  ┆   ┆ sue_topic ┆ y_illumin ┆ illuminat ┆ luminati │\n",
       "│ u32       ┆ _size |   ┆ ons |     ┆ Mean      ┆   ┆ _illumina ┆ ating |   ┆ ing |     ┆ ng |     │\n",
       "│           ┆ Mean      ┆ Mean      ┆ ---       ┆   ┆ tin…      ┆ StdD…     ┆ StdDev    ┆ StdDev   │\n",
       "│           ┆ ---       ┆ ---       ┆ f64       ┆   ┆ ---       ┆ ---       ┆ ---       ┆ ---      │\n",
       "│           ┆ f64       ┆ f64       ┆           ┆   ┆ f64       ┆ f64       ┆ f64       ┆ f64      │\n",
       "╞═══════════╪═══════════╪═══════════╪═══════════╪═══╪═══════════╪═══════════╪═══════════╪══════════╡\n",
       "│ 246745    ┆ 556462.85 ┆ 45601.525 ┆ 1061.2914 ┆ … ┆ 0.272697  ┆ 0.390334  ┆ 0.07984   ┆ 0.051297 │\n",
       "│           ┆ 5969      ┆ 952       ┆ 34        ┆   ┆           ┆           ┆           ┆          │\n",
       "└───────────┴───────────┴───────────┴───────────┴───┴───────────┴───────────┴───────────┴──────────┘"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Summary statistics\n",
    "df.select([\n",
    "    pl.len().alias(\"Row Count\"),\n",
    "    *[pl.col(c).mean().alias(f\"{c} | Mean\") for c in numeric_cols],\n",
    "    *[pl.col(c).min().alias(f\"{c} | Min\") for c in numeric_cols],\n",
    "    *[pl.col(c).max().alias(f\"{c} | Max\") for c in numeric_cols],\n",
    "    *[pl.col(c).std().alias(f\"{c} | StdDev\") for c in numeric_cols]\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bee3cabe-1dcf-44f2-bdc3-b69332aa00e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- page_id ---\n",
      "Unique count: 4475\n",
      "Skipped page_id: \"counts\" not found\n",
      "\n",
      "--- ad_id ---\n",
      "Unique count: 246745\n",
      "Skipped ad_id: \"counts\" not found\n",
      "\n",
      "--- ad_creation_time ---\n",
      "Unique count: 547\n",
      "Skipped ad_creation_time: \"counts\" not found\n",
      "\n",
      "--- bylines ---\n",
      "Unique count: 3791\n",
      "Skipped bylines: \"counts\" not found\n",
      "\n",
      "--- currency ---\n",
      "Unique count: 18\n",
      "Skipped currency: \"counts\" not found\n",
      "\n",
      "--- delivery_by_region ---\n",
      "Unique count: 141122\n",
      "Skipped delivery_by_region: \"counts\" not found\n",
      "\n",
      "--- demographic_distribution ---\n",
      "Unique count: 215622\n",
      "Skipped demographic_distribution: \"counts\" not found\n",
      "\n",
      "--- publisher_platforms ---\n",
      "Unique count: 9\n",
      "Skipped publisher_platforms: \"counts\" not found\n",
      "\n",
      "--- illuminating_scored_message ---\n",
      "Unique count: 26338\n",
      "Skipped illuminating_scored_message: \"counts\" not found\n",
      "\n",
      "--- illuminating_mentions ---\n",
      "Unique count: 278\n",
      "Skipped illuminating_mentions: \"counts\" not found\n"
     ]
    }
   ],
   "source": [
    "for col in non_numeric_cols:\n",
    "    try:\n",
    "        print(f\"\\n--- {col} ---\")\n",
    "        print(\"Unique count:\", df[col].n_unique())\n",
    "        display(df[col].value_counts().sort(\"counts\", descending=True).head(3))\n",
    "    except Exception as e:\n",
    "        print(f\"Skipped {col}: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e595b43-1a26-4a8b-92a1-1ed078d0e0e2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
