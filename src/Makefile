args=$(filter-out $@,$(MAKECMDGOALS))${1}

python:
	docker cp ./$(call args) py3minepi:/; docker exec -it py3minepi python /$(call args);