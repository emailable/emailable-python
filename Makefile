.PHONY: release

release:
ifndef VERSION
	$(error VERSION is required, e.g. make release VERSION=1.2.3)
endif
	@echo "$(VERSION)" | grep -Eq '^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$$' || { echo "error: VERSION must be x.y.z"; exit 1; }
	@test -z "$$(git status --porcelain)" || { echo "error: working tree not clean"; exit 1; }
	@test "$$(git branch --show-current)" = master || { echo "error: release from master"; exit 1; }
	@git fetch -q --tags origin master
	@! git rev-parse -q --verify "refs/tags/$(VERSION)" >/dev/null || { echo "error: tag $(VERSION) already exists"; exit 1; }
	@cur="$$(cat VERSION)"; [ "$$cur" != "$(VERSION)" ] && [ "$$(printf '%s\n' "$$cur" "$(VERSION)" | sort -V | tail -1)" = "$(VERSION)" ] || { echo "error: VERSION must be greater than $$cur"; exit 1; }
	@test "$$(git rev-parse HEAD)" = "$$(git rev-parse origin/master)" || { echo "error: master is not in sync with origin"; exit 1; }
	pytest
	@echo "$(VERSION)" > VERSION
	@git commit -q -am "Release $(VERSION)"
	@git tag -a $(VERSION) -m $(VERSION)
	@echo "Tagged $(VERSION). Push the commit and tag to release: git push --follow-tags"
