# -*- mode: makefile -*-
#
#--------------------------------------------------------------------------
# Variable definition
#--------------------------------------------------------------------------
#
# Use to differentiate makefile run on local vs CI
#
COMPOSE = MSYS_NO_PATHCONV=1 docker compose
DOCKER = MSYS_NO_PATHCONV=1 docker

#
#--------------------------------------------------------------------------
##@ Help
#--------------------------------------------------------------------------
#
.PHONY: help
help: ## Print this help with list of available commands/targets and their purpose
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

#
#--------------------------------------------------------------------------
##@ Docker Compose
#--------------------------------------------------------------------------
#
# Manage docker compose instances
#
.PHONY: up
up: pull ## Start the stack
	@$(COMPOSE) up -d

.PHONY: down
down: ## Stop the stack
	@$(COMPOSE) down --remove-orphans

.PHONY: pull
pull: ## Pull the latest images for the docker compose file
	@$(COMPOSE) pull

.PHONY: test
test: ## Run the tests
	@$(COMPOSE) run --rm flask-101 pytest
