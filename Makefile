.PHONY: commit-applications install-claude uninstall-claude help

CLAUDE_HOME ?= $(HOME)/.claude
REPO_ROOT   := $(shell pwd)

help:
	@echo "Available commands:"
	@echo "  make commit-applications   - Commit new application folders individually"
	@echo "  make install-claude        - Symlink claude/ preferences and skills into $(CLAUDE_HOME)"
	@echo "  make uninstall-claude      - Remove those symlinks"

commit-applications:
	@echo "Committing new application folders..."
	@git status --short resume/applications/ | grep "^??" | awk '{print $$2}' | sed 's|/.*||' | sort -u | while read folder; do \
		if [ -n "$$folder" ] && [ "$$folder" != "resume" ]; then \
			folder_name=$$(basename "$$folder"); \
			echo ""; \
			echo "Committing: $$folder_name"; \
			git add "$$folder/"; \
			git commit -m "chore(application): $$folder_name"; \
		fi; \
	done
	@echo ""
	@echo "✓ All application folders committed!"

# Symlinks rather than copies, so editing a file here takes effect immediately
# and this repo stays the single source of truth. Backs up anything already there.
install-claude:
	@mkdir -p "$(CLAUDE_HOME)"
	@if [ -e "$(CLAUDE_HOME)/CLAUDE.md" ] && [ ! -L "$(CLAUDE_HOME)/CLAUDE.md" ]; then \
		echo "Backing up existing CLAUDE.md -> CLAUDE.md.bak"; \
		mv "$(CLAUDE_HOME)/CLAUDE.md" "$(CLAUDE_HOME)/CLAUDE.md.bak"; \
	fi
	@ln -sfn "$(REPO_ROOT)/claude/CLAUDE.md" "$(CLAUDE_HOME)/CLAUDE.md"
	@if [ -e "$(CLAUDE_HOME)/skills" ] && [ ! -L "$(CLAUDE_HOME)/skills" ]; then \
		echo "$(CLAUDE_HOME)/skills exists and is a real directory - linking skills individually"; \
		for d in claude/skills/*/; do \
			ln -sfn "$(REPO_ROOT)/$$d" "$(CLAUDE_HOME)/skills/$$(basename $$d)"; \
		done; \
	else \
		ln -sfn "$(REPO_ROOT)/claude/skills" "$(CLAUDE_HOME)/skills"; \
	fi
	@echo "✓ Linked into $(CLAUDE_HOME):"
	@echo "    CLAUDE.md  -> claude/CLAUDE.md"
	@echo "    skills/    -> claude/skills/"
	@echo "  Preferences now apply in every repo. Per-project memory is untouched."

uninstall-claude:
	@for p in "$(CLAUDE_HOME)/CLAUDE.md" "$(CLAUDE_HOME)/skills"; do \
		if [ -L "$$p" ]; then rm "$$p"; echo "removed $$p"; fi; \
	done
	@for d in claude/skills/*/; do \
		p="$(CLAUDE_HOME)/skills/$$(basename $$d)"; \
		if [ -L "$$p" ]; then rm "$$p"; echo "removed $$p"; fi; \
	done
	@if [ -f "$(CLAUDE_HOME)/CLAUDE.md.bak" ]; then \
		mv "$(CLAUDE_HOME)/CLAUDE.md.bak" "$(CLAUDE_HOME)/CLAUDE.md"; \
		echo "restored CLAUDE.md from backup"; \
	fi
	@echo "✓ Uninstalled."
