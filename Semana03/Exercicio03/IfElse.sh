#!/bin/bash

if [ ${1,,} = rafael ]; then
	echo "Bem vindo Rafael!"
elif [ ${1,,} = help ]; then
	echo "Apenas digite seu nome corretamente!"
else 
	echo "Não sei quem é, mas você não está permitido!"
fi
	
