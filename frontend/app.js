// ─── Dynamic WebSocket URL ─────────────────────────────────────
// Works on localhost AND Render without changing this code.
const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const host     = window.location.host; // e.g. localhost:8000 or yourapp.onrender.com
const socket   = new WebSocket(`${protocol}//${host}/ws/live`);

// ─── Elements ──────────────────────────────────────────────────
const pill        = document.getElementById('live-pill');
const pillText    = document.getElementById('pill-text');
const lastUpdated = document.getElementById('last-updated');
const container   = document.getElementById('matches-container');

// ─── Helpers ───────────────────────────────────────────────────
function setStatus(state) {
    pill.className = 'live-pill';
    if (state === 'live') {
        pill.classList.add('');       // green by default
        pillText.textContent = 'LIVE';
    } else if (state === 'connecting') {
        pill.classList.add('connecting');
        pillText.textContent = 'CONNECTING';
    } else {
        pill.classList.add('disconnected');
        pillText.textContent = 'DISCONNECTED';
    }
}

function updateTimestamp() {
    const now = new Date();
    lastUpdated.textContent = `Updated ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;
}

function renderMatches(data) {
    if (!data.matches || data.matches.length === 0) {
        container.innerHTML = `<div class="match-card not-live">
            <div class="card-series no-match">IPL 2026</div>
            <p style="color:var(--muted); font-size:0.9rem;">No live matches right now. Check back soon.</p>
        </div>`;
        return;
    }

    container.innerHTML = '';

    data.matches.forEach((match, i) => {
        const isLive = match.isLive !== false;

        const card = document.createElement('div');
        card.className = `match-card${isLive ? '' : ' not-live'}`;
        card.style.animationDelay = `${i * 80}ms`;

        card.innerHTML = `
            <div class="card-series${isLive ? '' : ' no-match'}">
                ${match.seriesName || 'IPL 2026'}
            </div>

            <div class="teams-row">
                <div class="team-block left">
                    <div class="team-short">${match.team1Short || match.team1 || '—'}</div>
                    <div class="team-full">${match.team1 || ''}</div>
                    <div class="team-score">${match.score1 || ''}</div>
                </div>

                <div class="vs-divider">
                    <div class="vs-line"></div>
                    <div class="vs-text">VS</div>
                    <div class="vs-line"></div>
                </div>

                <div class="team-block right">
                    <div class="team-short">${match.team2Short || match.team2 || '—'}</div>
                    <div class="team-full">${match.team2 || ''}</div>
                    <div class="team-score">${match.score2 || ''}</div>
                </div>
            </div>

            <div class="card-status">
                <div class="status-dot ${isLive ? '' : 'inactive'}"></div>
                <span>${match.status || 'Live'}</span>
                <span class="match-desc">${match.matchDesc || ''}</span>
            </div>
        `;

        container.appendChild(card);
    });

    updateTimestamp();
}

// Team colors map
const TEAM_COLORS = {
    "MI":   "#004BA0", "CSK":  "#F9CD05", "RCB":  "#D1272A",
    "KKR":  "#3B2E7E", "DC":   "#0078BC", "PBKS": "#ED1B24",
    "RR":   "#FF69B4", "SRH":  "#F7A721", "LSG":  "#A4C4E0",
    "GT":   "#1C4F9C"
};

function getTeamColor(short) {
    return TEAM_COLORS[short] || "#334155";
}

function renderPointsTable(teams) {
    const container = document.getElementById('points-table-container');
    if (!container) return;

    if (!teams || teams.length === 0) {
        container.innerHTML = `<p style="color:var(--muted); padding:16px;">Points table not available.</p>`;
        return;
    }

    let html = `<div class="points-table">
        <div class="pt-header">
            <div>Team</div>
            <div style="text-align:center">P</div>
            <div style="text-align:center">W</div>
            <div style="text-align:center">L</div>
            <div style="text-align:center">NR</div>
            <div style="text-align:center">PTS</div>
            <div style="text-align:center">NRR</div>
        </div>`;

    // Playoff zone label after 4th team
    teams.forEach((team, i) => {
        if (i === 4) {
            html += `<div class="playoff-label">▲ PLAYOFF ZONE</div>`;
        }

        const isPlayoff = i < 4;
        const nrrVal = parseFloat(team.nrr) || 0;
        const nrrClass = nrrVal > 0 ? 'positive' : nrrVal < 0 ? 'negative' : '';
        const nrrDisplay = nrrVal > 0 ? `+${team.nrr}` : team.nrr;
        const color = getTeamColor(team.teamName);

        html += `
        <div class="pt-row${isPlayoff ? ' playoff' : ''}" style="animation-delay:${i * 40}ms">
            <div class="pt-team">
                <div class="team-badge" style="background:${color}">${team.teamName}</div>
                <div>
                    <div class="pt-team-name">${team.teamName}</div>
                    <div class="pt-team-full">${team.teamFullName}</div>
                </div>
            </div>
            <div class="pt-cell">${team.played}</div>
            <div class="pt-cell">${team.won}</div>
            <div class="pt-cell">${team.lost}</div>
            <div class="pt-cell">${team.noResult}</div>
            <div class="pt-cell points">${team.points}</div>
            <div class="pt-cell nrr ${nrrClass}">${nrrDisplay}</div>
        </div>`;
    });

    html += `</div>`;
    container.innerHTML = html;
}


socket.onopen = () => {
    console.log('✅ Connected to backend');
    setStatus('live');
};

socket.onmessage = (event) => {
    try {
        const data = JSON.parse(event.data);
        console.log('📡 Data received:', data);
        renderMatches(data);
        if (data.pointsTable) renderPointsTable(data.pointsTable);
    } catch (err) {
        console.error('Parse error:', err);
    }
};

socket.onclose = () => {
    console.warn('❌ Disconnected');
    setStatus('disconnected');
};

socket.onerror = (err) => {
    console.error('WebSocket error:', err);
    setStatus('disconnected');
};