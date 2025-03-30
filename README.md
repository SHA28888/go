Her er en detaljert README-fil for ditt Go-prosjekt, inkludert all informasjon vi har diskutert:

```markdown
# Go-prosjekt

Dette er et eksempelprosjekt for Go-språket.

## Innholdsfortegnelse

- [Introduksjon](#introduksjon)
- [Telegram-bot](#telegram-bot)
  - [Opprett en Telegram-bot](#opprett-en-telegram-bot)
  - [Sett opp prosjektet](#sett-opp-prosjektet)
  - [Installer nødvendige avhengigheter](#installer-nødvendige-avhengigheter)
  - [Start boten](#start-boten)
- [To-do list applikasjon](#to-do-list-applikasjon)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
- [Node.js server](#nodejs-server)
  - [Filstruktur](#filstruktur)
  - [Installasjon](#installasjon)
  - [Start serveren](#start-serveren)
- [Bidra](#bidra)
- [Lisens](#lisens)
- [Kontakt](#kontakt)

## Introduksjon

Dette prosjektet er utviklet for å demonstrere grunnleggende funksjonaliteter i Go, samt integrasjon med en Telegram-bot og en enkel to-do list applikasjon.

## Telegram-bot

### Opprett en Telegram-bot

1. Åpne Telegram og søk etter *@BotFather*.
2. Start samtalen med kommando `/start`.
3. Skriv `/newbot` og følg instruksjonene:
   - Først gi boten et navn, f.eks. «Min TestBot».
   - Deretter gi boten et unikt brukernavn som må ende med «bot», f.eks. «MinTestBot_bot».
4. Du vil motta en API-token. Notér denne, du trenger den senere.

Eksempel på API-token:
```
1234567890:ABCdefGhIJKlmNOP_qrstuvwXyz
```

### Sett opp prosjektet

Opprett en katalogstruktur i ditt eksisterende GitHub-repo slik:

```
telegram-promoting-page/
├── bots/
│   └── norskTelegramBot.js
│   └── README.md
│   └── package.json
│
├── todo-app/
│   └── index.html
│   └── css/
│   │   └── style.css
│   └── js/
│   │   └── main.js
│   └── README.md
│
├── server/
│   └── server.js
│   └── package.json
│   └── .env
│   └── README.md
│
├── .gitignore
└── README.md
```

### Installer nødvendige avhengigheter

For å bruke eksempelet ovenfor, må du installere pakkene med npm:

```bash
npm init -y
npm install telegraf
```

### Start boten

1. Sørg for at du har Node.js installert på maskinen din.
2. Naviger til mappen der du har lagret bot-filene.
3. Installer nødvendige pakker:
   ```bash
   npm install telegraf
   ```
4. Start boten:
   ```bash
   node bots/norskTelegramBot.js
   ```
5. Boten din er nå aktiv og klar til bruk! Søk etter den i Telegram med bot-brukernavnet ditt.

Bot-token er allerede inkludert i koden. For sikkerhets skyld burde du vurdere å flytte token til en separat miljøvariabel i en produksjonsmiljø.

## To-do list applikasjon

### HTML

```html
<!DOCTYPE html>
<html lang="nb">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gjøremålsliste</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Min Gjøremålsliste</h1>
        
        <div class="input-section">
            <input type="text" id="oppgaveInput" placeholder="Skriv inn ny oppgave...">
            <button id="leggTilKnapp">Legg til</button>
        </div>

        <div class="filter-section">
            <button class="filter-btn active" data-filter="alle">Alle</button>
            <button class="filter-btn" data-filter="aktive">Aktive</button>
            <button class="filter-btn" data-filter="fullført">Fullført</button>
        </div>

        <ul id="oppgaveliste"></ul>

        <div class="info-section">
            <p>Gjenstående oppgaver: <span id="gjenstaende">0</span></p>
            <button id="slettFullforteKnapp">Slett fullførte</button>
        </div>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
```

### CSS

```css
:root {
    --primary-color: #00507A; /* Norsk blå */
    --secondary-color: #CF2D35; /* Norsk rød */
    --background-color: #F0F5F9;
    --text-color: #2C3E50;
}

body {
    font-family: 'Arial', sans-serif;
    background-color: var(--background-color);
    margin: 0;
    padding: 20px;
    color: var(--text-color);
}

.container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: var(--primary-color);
    text-align: center;
    margin-bottom: 30px;
}

.input-section {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

input[type="text"] {
    flex: 1;
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

button {
    background-color: var(--primary-color);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #003857;
}

.filter-section {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
}

.filter-btn {
    background-color: #eee;
    color: var(--text-color);
}

.filter-btn.active {
    background-color: var(--primary-color);
    color: white;
}

#oppgaveliste {
    list-style: none;
    padding: 0;
}

.oppgave-element {
    display: flex;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
    gap: 10px;
}

.oppgave-element.fullfort {
    background-color: #f8f9fa;
}

.oppgave-element.fullfort span {
    text-decoration: line-through;
    color: #6c757d;
}

.slett-knapp {
    background-color: var(--secondary-color);
    padding: 5px 10px;
    margin-left: auto;
}

.info-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}

#slettFullforteKnapp {
    background-color: var(--secondary-color);
}

#slettFullforteKnapp:hover {
    background-color: #b71c1c;
}
```

### JavaScript

```javascript
class Oppgaveliste {
    constructor() {
        this.oppgaver = JSON.parse(localStorage.getItem('oppgaver')) || [];
        this.aktivFilter = 'alle';
        this.initializeEventListeners();
        this.oppdaterVisning();
    }

    initializeEventListeners() {
        // Input og legg til knapp
        document.getElementById('leggTilKnapp').addEventListener('click', () => this.leggTilOppgave());
        document.getElementById('oppgaveInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.leggTilOppgave();
        });

        // Filter knapper
        document.querySelectorAll('.filter-btn').forEach(knapp => {
            knapp.addEventListener('click', (e) => {
                this.aktivFilter = e.target.dataset.filter;
                this.oppdaterFilterKnapper();
                this.oppdaterVisning();
            });
        });

        // Slett fullførte knapp
        document.getElementById('slettFullforteKnapp').addEventListener('click', () => {
            this.slettFullforteOppgaver();
        });
    }

    leggTilOppgave() {
        const input = document.getElementById('oppgaveInput');
        const tekst = input.value.trim();

        if (tekst) {
            const nyOppgave = {
                id: Date.now(),
                tekst: tekst,
                fullfort: false,
                dato: new Date().toLocaleDateString('nb-NO')
            };

            this.oppgaver.push(nyOppgave);
            this.lagreOppgaver();
            this.oppdaterVisning();
            input.value = '';
        }
    }

    toggleOppgaveStatus(id) {
        const oppgave = this.oppgaver.find(o => o.id === id);
        if (oppgave) {
            oppgave.fullfort = !oppgave.fullfort;
            this.lagreOppgaver();
            this.oppdaterVisning();
        }
    }

    slettOppgave(id) {
        this.oppgaver = this.oppgaver.filter(oppgave => oppgave.id !== id);
        this.lagreOppgaver();
        this.oppdaterVisning();
    }

    slettFullforteOppgaver() {
        this.oppgaver = this.oppgaver.filter(oppgave => !oppgave.fullfort);
        this.lagreOppgaver();
        this.oppdaterVisning();
    }

    filtrerOppgaver() {
        switch (this.aktivFilter) {
            case 'aktive':
                return this.oppgaver.filter(oppgave => !oppgave.fullfort);
            case 'fullført':
                return this.oppgaver.filter(oppgave => oppgave.fullfort);
            default:
                return this.oppgaver;
        }
    }

    oppdaterFilterKnapper() {
        document.querySelectorAll('.filter-btn').forEach(knapp => {
            knapp.classList.toggle('active', knapp.dataset.filter === this.aktivFilter);
        });
    }

    oppdaterVisning() {
        const liste = document.getElementById('oppgaveliste');
        const filtrerteOppgaver = this.filtrerOppgaver();
        
        liste.innerHTML = '';
        
        filtrerteOppgaver.forEach(oppgave => {
            const li = document.createElement('li');
            li.className = `oppgave-element ${oppgave.fullfort ? 'fullfort' : ''}`;
            
            li.innerHTML = `
                <input type="checkbox" ${oppgave.fullfort ? 'checked' : ''}>
                <span>${oppgave.tekst}</span>
                <small>${oppgave.dato}</small>
                <button class="slett-knapp">Slett</button>
            `;

            const checkbox = li.querySelector('input[type="checkbox"]');
            checkbox.addEventListener('change', () => this.toggleOppgaveStatus(oppgave.id));

            const slettKnapp = li.querySelector('.slett-knapp');
            slettKnapp.addEventListener('click', () => this.slettOppgave(oppgave.id));

            liste.appendChild(li);
        });

        // Oppdater antall gjenstående oppgaver
        const gjenstaende = this.oppgaver.filter(oppgave => !oppgave.fullfort).length;
        document.getElementById('gjenstaende').textContent = gjenstaende;
    }

    lagreOppgaver() {
        localStorage.setItem('oppgaver', JSON.stringify(this.oppgaver));
    }
}

// Initialiser applikasjonen
const oppgaveliste = new Oppgaveliste();
```

## Node.js server

### Filstruktur

Opprett følgende katalogstruktur:

```
server/
├── src/
│   └── server.js
├── package.json
├── .env
└── README.md
```

### Installasjon

Naviger til `server`-mappen og installer avhengigheter:

```bash
cd server
npm install
```

### Start serveren

Start serveren med:

```bash
npm start
```

Eller i utviklingsmodus med automatisk restart:

```bash
npm run dev
```

Serveren er nå tilgjengelig på `http://localhost:3000`.

## Bidra

Bidrag er alltid velkomne! Følg disse trinnene for å bidra:

1. Fork dette repositoriet.
2. Opprett en ny branch: `git checkout -b feature-navn`.
3. Gjør endringer og commit: `git commit -m 'Legg til noe nytt'`.
4. Push til branchen: `git push origin feature-navn`.
5. Opprett en pull request.

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen. Se [LICENSE](LICENSE) for mer informasjon.

## Kontakt

Hvis du har spørsmål eller forslag, vennligst kontakt meg via [e-post](mailto:din.email@domain.com).

---

Lykke til med ditt Go-prosjekt!
```

Denne README-filen inkluderer all informasjonen vi har diskutert, og er optimalisert for norske brukere. Du kan kopiere denne teksten og lime den inn i `README.md`-filen din i GitHub-repositoriet. Hvis du trenger ytterligere tilpasninger eller har andre spørsmål, er det bare å gi beskjed!
