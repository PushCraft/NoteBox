# GitHub setup for NoteBox

This project is a scaffold, not a functioning deployed notes app.

## New repository
Create an empty **private** repository named `notebox` under `PushCraft`. Avoid generating a GitHub README when creating the repository because this project already has one.

```bash
cd notebox
git init
git add .
git commit -m "Initial NoteBox project scaffold"
git branch -M main
git remote add origin git@github.com:PushCraft/notebox.git
git push -u origin main
```

## If you already pushed the old CloudDrop repository
Rename the existing repository in GitHub Settings > General > Repository name to `notebox`, then in your existing local folder:

```bash
git remote set-url origin git@github.com:PushCraft/notebox.git
git remote -v
```

Then apply the renamed scaffold files to your existing repository and commit them. Do **not** run `git init` in an existing repository or overwrite local changes without reviewing them.

## Next milestone
Implement the local Python API and frontend interaction, add tests, then provision AWS resources incrementally.
