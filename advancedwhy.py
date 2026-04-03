import os

def generate_scene_document():
    """
    Outputs the essay to the terminal AND saves it to a permanent text file.
    """
    
    title = "THE ART OF THE CRACK: A PERSONAL PERSPECTIVE"
    border = "=" * len(title)
    
    content = (
        f"{border}\n"
        f"{title}\n"
        f"{border}\n\n"
        "For me, the world of digital piracy isn't just about getting content for free; "
        "it’s a deep fascination with the technical mastery and rebellious spirit of the scene. "
        "I find myself captivated by the legendary history of groups like Razor1911, who "
        "set the standard for subculture and style, and CPY, whose breakthrough cracks of "
        "games like Resident Evil 7 proved that no digital lock is truly permanent.\n\n"
        
        "Seeing CODEX deliver flawless releases for massive titles like God of War or "
        "Forza Horizon 5 felt like watching master craftsmen at work, ensuring that a "
        "piece of software was optimized and preserved without the bloat of restrictive DRM.\n\n"
        
        "Following the exploits of individuals like EMPRESS as they dismantle supposedly "
        "'uncrackable' versions of Red Dead Redemption 2 or Hogwarts Legacy is like watching "
        "a high-stakes chess match played in pure code. It has influenced the way I look "
        "at software; I don’t just see a game, I see the intricate logic and the battle "
        "of wits happening under the hood. For someone who appreciates how hardware and "
        "software interact, these crackers represent the ultimate level of reverse-engineering.\n\n"
        
        "They’ve taught me to value digital ownership and the importance of optimization, "
        "turning my interest in gaming into a genuine respect for the elite-level coding "
        "that keeps the 'all-in-one' library accessible and alive.\n"
    )

    # 1. Print to Terminal (for immediate view)
    print(content)

    # 2. Save to File (for permanent output)
    file_name = "Scene_Legacy.txt"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n[SUCCESS] Document saved as: {os.path.abspath(file_name)}")
    except Exception as e:
        print(f"\n[ERROR] Could not save file: {e}")

if __name__ == "__main__":
    generate_scene_document()
#NOT WORKING
