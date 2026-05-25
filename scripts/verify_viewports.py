import asyncio
import os
from playwright.async_api import async_playwright

async def capture_viewports(url, name, output_dir):
    viewports = [
        {"name": "desktop", "width": 1920, "height": 1080},
        {"name": "ipad", "width": 820, "height": 1180},
        {"name": "mobile", "width": 390, "height": 844},
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        
        # Determine relative path if it's a file
        full_url = url
        if not url.startswith("http"):
             full_url = f"file://{os.path.abspath(url)}"

        for vp in viewports:
            await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
            await page.goto(full_url, wait_until="networkidle")
            # Wait a bit for animations etc
            await asyncio.sleep(1)
            filename = f"{name}_{vp['name']}.png"
            path = os.path.join(output_dir, filename)
            await page.screenshot(path=path, full_page=True)
            print(f"Captured {path}")

        await browser.close()

async def main():
    base_dir = "/root/projects/sports-raise"
    output_dir = os.path.join(base_dir, "docs/screenshots")
    os.makedirs(output_dir, exist_ok=True)
    
    files_to_check = [
        "landing-page.html",
        "campaign.html",
        "dashboards.html",
        "onboarding.html"
    ]
    
    for html_file in files_to_check:
        path = os.path.join(base_dir, html_file)
        if os.path.exists(path):
            name = html_file.replace(".html", "")
            await capture_viewports(path, name, output_dir)

if __name__ == "__main__":
    asyncio.run(main())
