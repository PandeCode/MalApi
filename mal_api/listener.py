#!/bin/env python3
import ctypes
from multiprocessing import Process, Manager, Value
from flask import Flask, request
from time import sleep


def flaskKeepQuite():
	import logging, click
	import typing as t

	log = logging.getLogger("werkzeug")
	log.setLevel(logging.ERROR)

	def echo(
		message: t.Optional[t.Any] = None,
		file: t.Optional[t.IO] = None,
		nl: bool = True,
		err: bool = False,
		color: t.Optional[bool] = None,
		**styles: t.Any,
	) -> None:
		pass

	click.echo = echo
	click.secho = echo


def getCode(port: int = 8000) -> str:
	flaskKeepQuite()

	app = Flask("ServiceShouldStop")
	server = Process(target=lambda: app.run(port=port))
	manager = Manager()

	code = manager.Value(ctypes.c_char_p, "")
	shouldKill = Value("b", False)

	@app.get("/callback")
	def callback():
		code.value = request.args.get("code") or ""
		shouldKill.value = code.value != ""
		return "Done"

	server.start()

	while not shouldKill.value:
		sleep(1)

	server.terminate()
	server.join()

	return code.value


if __name__ == "__main__":
	print("Hello")
	print(getCode())
	print("World")
