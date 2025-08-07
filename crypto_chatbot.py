bot_name = "CryptoBuddy"
bot_intro = "👋 Hey there! I’m CryptoBuddy — your AI-powered crypto sidekick. Ready to help you invest smartly and sustainably!"




crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}


def get_user_input():
    return input("\nYou: ").lower()

def respond_to_query(query):
    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"{bot_name}: Invest in {best}! It’s eco-friendly and has long-term potential."
    
    elif "trending" in query or "growth" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]]
        if trending:
            return f"{bot_name}: {', '.join(trending)} are trending up! Great options for growth!"
        else:
            return f"{bot_name}: Hmm, nothing's booming right now."

    elif "energy" in query:
        energy_eff = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"{bot_name}: {', '.join(energy_eff)} uses the least energy! "

    elif "recommend" in query or "buy" in query:
        best = None
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"] and data["sustainability_score"] > 0.7:
                best = coin
        if best:
            return f"{bot_name}: You should consider buying {best}. It’s growing and green!"
        else:
            return f"{bot_name}: I'm not seeing any perfect fit right now. Do more research!"

    elif "disclaimer" in query or "risk" in query:
        return f"{bot_name}: Crypto is risky—always do your own research before investing!"

    else:
        return f"{bot_name}: I’m not sure about that. Try asking about trending coins, sustainability, or recommendations."



print(bot_intro)

while True:
    user_query = get_user_input()
    
    if user_query in ["exit", "quit", "bye"]:
        print(f"{bot_name}: See you soon, and invest wisely! 👋")
        break
    
    response = respond_to_query(user_query)
    print(response)


