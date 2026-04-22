.PHONY: commit-applications help

help:
	@echo "Available commands:"
	@echo "  make commit-applications   - Commit new application folders individually"

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
