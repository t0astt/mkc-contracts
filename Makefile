compile: clean
	brownie compile

clean:
	rm -rf build/

deploy_local:
	brownie run scripts/deploy.py
