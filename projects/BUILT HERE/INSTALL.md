# INSTALL.md

## Safe replacement procedure

### 1. In Terminal, paste this:

```bash
cd ~/AI/ai-learning-lab/projects
cp -R "BUILT HERE" "BUILT HERE BACKUP 2026-07-17"
```

### 2. In Finder

Open:

`~/AI/ai-learning-lab/projects/BUILT HERE`

Delete the contents inside the folder, but keep the `BUILT HERE` folder itself.

Copy every item from this package into the empty `BUILT HERE` folder.

### 3. In Terminal, paste this:

```bash
cd ~/AI/ai-learning-lab/projects/"BUILT HERE"
git status
git add .
git commit -m "Install Built Here repository v1.0"
git push
```

### 4. In Hermes

Open this repository and paste the contents of `HERMES_STARTUP_PROMPT.md` into the Hermes chat.
