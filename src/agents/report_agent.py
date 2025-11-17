# src/agents/report_agent.py
import markdown
import pdfkit
from loguru import logger

def compose_markdown_report(title, summary, insights_text, image_paths):
    md = f"# {title}\n\n"
    md += "## Summary\n\n"
    md += "```\n" + str(summary) + "\n```\n\n"
    md += "## Insights\n\n" + insights_text + "\n\n"
    md += "## Visualizations\n\n"
    for p in image_paths:
        md += f"![{p}]({p})\n\n"
    return md

def save_pdf_from_markdown(md_text, out_pdf_path):
    html = markdown.markdown(md_text)
    pdfkit.from_string(html, out_pdf_path)
    logger.info(f"PDF saved to {out_pdf_path}")
