.PHONY: help run setup format
# 😄 ✨ 👍 🔥 🐳(docker) 🌟 🏄 ✋(stop) 🛑 (off)

help: # —————————— 도움말
	@echo "——————————————————————————————————————————————————"
	@cat Makefile | grep "# —————" | grep -v "grep"  | awk -F": #" '{ printf("• \033[1;32m%-30s\033[0m %s\n",$$1, $$2)}'
	@echo "——————————————————————————————————————————————————"

mongo-up: # —————————— mongodb
	docker run --name mongodb-container -v /tmp/mongo:/data/db -d -p 27017:27017 mongo

