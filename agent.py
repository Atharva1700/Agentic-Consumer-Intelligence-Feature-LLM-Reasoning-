#!/usr/bin/env python3
"""Agentic consumer intelligence: ingests video metadata, surfaces emerging patterns."""

import json
from typing import Any
from dataclasses import dataclass
from anthropic import Anthropic

# ponytail: Single agent file, no separate orchestration layer needed until scale demands it

@dataclass
class VideoMetadata:
    id: str
    title: str
    views: int
    engagement_rate: float
    hashtags: list[str]
    sentiment: str

# Simulated batch of short-form video metadata
SAMPLE_VIDEOS = [
    VideoMetadata("v1", "AI productivity hack", 150000, 0.084, ["#ai", "#productivity", "#work"], "positive"),
    VideoMetadata("v2", "GenAI workflow tips", 200000, 0.091, ["#genai", "#workflow", "#productivity"], "positive"),
    VideoMetadata("v3", "Claude saves my day", 120000, 0.079, ["#claude", "#ai", "#work"], "positive"),
    VideoMetadata("v4", "Fitness transformation", 350000, 0.112, ["#fitness", "#motivation", "#health"], "positive"),
    VideoMetadata("v5", "AI in healthcare", 180000, 0.088, ["#ai", "#healthcare", "#innovation"], "positive"),
    VideoMetadata("v6", "Gaming on budget", 220000, 0.098, ["#gaming", "#budget", "#streaming"], "positive"),
    VideoMetadata("v7", "LLM code generation", 140000, 0.082, ["#ai", "#coding", "#productivity"], "positive"),
]

def ingest_batch() -> dict:
    """Ingest batch of video metadata."""
    return {
        "videos": [
            {
                "id": v.id,
                "title": v.title,
                "views": v.views,
                "engagement_rate": v.engagement_rate,
                "hashtags": v.hashtags,
                "sentiment": v.sentiment,
            }
            for v in SAMPLE_VIDEOS
        ],
        "batch_size": len(SAMPLE_VIDEOS),
    }

def analyze_patterns(batch: dict) -> dict:
    """Run multi-step reasoning to surface emerging patterns."""
    videos = batch["videos"]
    
    # Aggregate hashtags by frequency
    tag_freq = {}
    for v in videos:
        for tag in v["hashtags"]:
            tag_freq[tag] = tag_freq.get(tag, 0) + 1
    
    # Correlation: views vs engagement
    total_views = sum(v["views"] for v in videos)
    total_engagement = sum(v["views"] * v["engagement_rate"] for v in videos)
    avg_engagement = total_engagement / total_views if total_views > 0 else 0
    
    return {
        "tag_frequencies": sorted(tag_freq.items(), key=lambda x: x[1], reverse=True),
        "avg_engagement_rate": round(avg_engagement, 3),
        "total_views": total_views,
        "video_count": len(videos),
    }

def generate_insight(client: Anthropic, analysis: dict) -> str:
    """Use Claude to synthesize actionable insight for marketing stakeholder."""
    prompt = f"""You are a consumer intelligence analyst. Based on this video batch analysis:

Tag frequencies (top topics):
{json.dumps(analysis['tag_frequencies'][:5], indent=2)}

Metrics:
- Average engagement rate: {analysis['avg_engagement_rate']:.1%}
- Total views: {analysis['total_views']:,}
- Videos analyzed: {analysis['video_count']}

In 2-3 sentences, identify ONE emerging pattern a marketing team should act on immediately.
Format: Pattern: [name]. Action: [specific, concrete step]. Priority: [high/medium].
"""
    
    response = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    
    return response.content[0].text

def main():
    client = Anthropic()
    
    # Step 1: Ingest batch
    print("📊 Ingesting video metadata batch...")
    batch = ingest_batch()
    print(f"✓ Loaded {batch['batch_size']} videos\n")
    
    # Step 2: Multi-step reasoning (pattern analysis)
    print("🔍 Analyzing patterns...")
    analysis = analyze_patterns(batch)
    print(f"✓ Top tag: {analysis['tag_frequencies'][0][0]} (appears {analysis['tag_frequencies'][0][1]}x)")
    print(f"✓ Average engagement: {analysis['avg_engagement_rate']:.1%}\n")
    
    # Step 3: LLM reasoning for actionable insight
    print("💡 Synthesizing actionable insight...")
    insight = generate_insight(client, analysis)
    print(f"✓ Insight:\n{insight}\n")
    
    # Structured output for stakeholder
    output = {
        "insight": insight,
        "metrics": {
            "total_videos_analyzed": analysis["video_count"],
            "total_views": analysis["total_views"],
            "avg_engagement": analysis["avg_engagement_rate"],
            "top_tags": [{"tag": t, "frequency": f} for t, f in analysis["tag_frequencies"][:3]],
        },
    }
    
    print("📤 Structured output for stakeholder:")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
