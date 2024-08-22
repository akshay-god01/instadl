import instaloader

L = instaloader.Instaloader()
username = 'instadl6'  # Replace with your Instagram username

try:
    L.load_session_from_file(username=username, filename='session-instagram')
    print("Session loaded successfully.")
except Exception as e:
    print(f"Failed to load session: {e}")

# Test with a known Instagram URL
url = "https://www.instagram.com/reel/C-2zD8IuU75/?igsh=eHo0MXkzN3Zubjc4"  # Replace with a valid shortcode
try:
    # Extract shortcode based on URL type
    if 'instagram.com/p/' in url:
        match = re.search(r'/p/([^/?]+)', url)
    else:
        print("Unsupported URL format.")
        exit(1)

    if not match:
        print("Failed to extract shortcode.")
        exit(1)

    shortcode = match.group(1)
    print(f"Extracted Shortcode: {shortcode}")

    post = instaloader.Post.from_shortcode(L.context, shortcode)
    print(f"Caption: {post.caption}")
    print(f"Likes: {post.likes}")

    if post.is_video:
        print(f"Video URL: {post.video_url}")
    else:
        print(f"Image URL: {post.url}")

except Exception as e:
    print(f"Error: {e}")
