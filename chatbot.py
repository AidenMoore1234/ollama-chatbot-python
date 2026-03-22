import requests

MODEL = "qwen3:4b"  # 如拉取了更小模型，改成对应名称
API_URL = "http://127.0.0.1:11434/api/chat"

def chat_once(prompt: str) -> str:
    """Send one prompt to the model and return the response text."""
    resp = requests.post(
        API_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]

def main() -> None:
    print("输入提问（输入“再见”退出）：")
    while True:
        user_input = input("> ").strip()
        if user_input == "再见":
            print("再见！")
            break
        if not user_input:
            continue
        try:
            reply = chat_once(user_input)
            print("Qwen:", reply)
        except requests.RequestException as exc:
            print(f"请求失败：{exc}")

if __name__ == "__main__":
    main()