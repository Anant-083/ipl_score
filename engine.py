import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_TOKEN")
API_HOST = os.getenv("API_HOST")

async def get_live_scores():
    url = f"https://{API_HOST}/matches/live"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=15.0)

            if response.status_code != 200:
                return {
                    "matches": [{
                        "title": "API Error",
                        "team1": "—", "score1": "",
                        "team2": "—", "score2": "",
                        "status": f"HTTP {response.status_code} — Check your API Key/Host in .env",
                        "matchDesc": "",
                        "seriesName": "",
                        "isLive": False
                    }]
                }

            data = response.json()
            matches = []

            IPL_KEYWORDS = ["IPL", "INDIAN PREMIER LEAGUE"]
            TEAM_SHORTS = {
                "MUMBAI": "MI", "CHENNAI": "CSK", "KOLKATA": "KKR",
                "RAJASTHAN": "RR", "DELHI": "DC", "PUNJAB": "PBKS",
                "HYDERABAD": "SRH", "SUNRISERS": "SRH", "BANGALORE": "RCB",
                "BENGALURU": "RCB", "LUCKNOW": "LSG", "GUJARAT": "GT"
            }

            def get_short(name):
                upper = name.upper()
                for key, short in TEAM_SHORTS.items():
                    if key in upper:
                        return short
                return name[:3].upper()

            for match_type in data.get('typeMatches', []):
                for series in match_type.get('seriesMatches', []):
                    wrapper = series.get('seriesAdWrapper', series)
                    series_name = wrapper.get('seriesName', '')

                    if not any(k in series_name.upper() for k in IPL_KEYWORDS):
                        continue

                    for m in wrapper.get('matches', []):
                        mi = m.get('matchInfo', m)
                        ms = m.get('matchScore', {})

                        t1_name = mi.get('team1', {}).get('teamName', 'TBD')
                        t2_name = mi.get('team2', {}).get('teamName', 'TBD')

                        t1_score = ms.get('team1Score', {})
                        t2_score = ms.get('team2Score', {})

                        def fmt_score(sc):
                            inn = sc.get('inngs1', {})
                            if inn:
                                runs = inn.get('runs', '')
                                wkts = inn.get('wickets', '')
                                overs = inn.get('overs', '')
                                if runs != '':
                                    wkt_str = f"/{wkts}" if wkts != '' and int(str(wkts)) < 10 else ""
                                    return f"{runs}{wkt_str} ({overs} ov)"
                            return ""

                        matches.append({
                            "title": f"{t1_name} vs {t2_name}",
                            "team1": t1_name,
                            "team1Short": get_short(t1_name),
                            "score1": fmt_score(t1_score),
                            "team2": t2_name,
                            "team2Short": get_short(t2_name),
                            "score2": fmt_score(t2_score),
                            "status": m.get('status', mi.get('status', 'Live')),
                            "matchDesc": mi.get('matchDesc', 'T20'),
                            "seriesName": series_name,
                            "isLive": True
                        })

            if not matches:
                upcoming = await get_upcoming_matches()
                if upcoming:
                    return {"matches": upcoming}
                return {
                    "matches": [{
                        "title": "No IPL Matches Right Now",
                        "team1": "—", "team1Short": "—", "score1": "",
                        "team2": "—", "team2Short": "—", "score2": "",
                        "status": "No IPL matches live or upcoming",
                        "matchDesc": "", "seriesName": "IPL 2026",
                        "isLive": False
                    }]
                }

            return {"matches": matches}

    except Exception as e:
        return {
            "matches": [{
                "title": "Connection Error",
                "team1": "—", "team1Short": "—", "score1": "",
                "team2": "—", "team2Short": "—", "score2": "",
                "status": str(e),
                "matchDesc": "", "seriesName": "",
                "isLive": False
            }]
        }


async def get_points_table():
    SERIES_ID = "9241"
    url = f"https://{API_HOST}/series/{SERIES_ID}/pointtable"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=15.0)
            if response.status_code != 200:
                return []
            data = response.json()
            teams = []
            for group in data.get('pointsTable', []):
                for entry in group.get('pointsTableInfo', []):
                    teams.append({
                        "teamName": entry.get('teamName', ''),
                        "teamFullName": entry.get('teamFullName', ''),
                        "played": entry.get('matchesPlayed', 0),
                        "won": entry.get('matchesWon', 0),
                        "lost": entry.get('matchesLost', 0),
                        "noResult": entry.get('noRes', 0),
                        "points": entry.get('points', 0),
                        "nrr": entry.get('nrr', '0.000'),
                    })
            teams.sort(key=lambda x: (int(x['points']), float(x['nrr'])), reverse=True)
            return teams
    except Exception:
        return []


async def get_upcoming_matches():
    url = f"https://{API_HOST}/matches/upcoming"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    IPL_KEYWORDS = ["IPL", "INDIAN PREMIER LEAGUE"]
    TEAM_SHORTS = {
        "MUMBAI": "MI", "CHENNAI": "CSK", "KOLKATA": "KKR",
        "RAJASTHAN": "RR", "DELHI": "DC", "PUNJAB": "PBKS",
        "HYDERABAD": "SRH", "SUNRISERS": "SRH", "BANGALORE": "RCB",
        "BENGALURU": "RCB", "LUCKNOW": "LSG", "GUJARAT": "GT"
    }

    def get_short(name):
        upper = name.upper()
        for key, short in TEAM_SHORTS.items():
            if key in upper:
                return short
        return name[:3].upper()

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=15.0)
            if response.status_code != 200:
                return []
            data = response.json()
            matches = []
            for match_type in data.get('typeMatches', []):
                for series in match_type.get('seriesMatches', []):
                    wrapper = series.get('seriesAdWrapper', series)
                    series_name = wrapper.get('seriesName', '')
                    if not any(k in series_name.upper() for k in IPL_KEYWORDS):
                        continue
                    for m in wrapper.get('matches', []):
                        mi = m.get('matchInfo', m)
                        t1 = mi.get('team1', {}).get('teamName', 'TBD')
                        t2 = mi.get('team2', {}).get('teamName', 'TBD')
                        matches.append({
                            "title": f"{t1} vs {t2}",
                            "team1": t1, "team1Short": get_short(t1), "score1": "",
                            "team2": t2, "team2Short": get_short(t2), "score2": "",
                            "status": f"Upcoming · {mi.get('matchDesc', 'T20')}",
                            "matchDesc": mi.get('matchDesc', 'T20'),
                            "seriesName": series_name,
                            "isLive": False
                        })
            return matches[:5]
    except Exception:
        return []