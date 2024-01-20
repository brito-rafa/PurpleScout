IMG ?= ghcr.io/lasarobotics/purple-scout:latest
.PHONY: build
build: ## Build Docker
	docker buildx build . -t ${IMG}

.PHONY: push
push: build ## push docker image
	docker push ${IMG}

.PHONY: run
run: ## Build Docker
	docker run -p 5000:5000 ${IMG}

