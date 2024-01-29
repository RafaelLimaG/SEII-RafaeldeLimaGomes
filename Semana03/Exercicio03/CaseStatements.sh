#!/bin/bash
case ${1,,} in
	Rafael | rafael | administrator )
		            echo "Bem vindo!"
			    ;;
	help)
		echo "Apenas informe seu nome"
		;;
	*)
		echo "Nome incorreto, entre com um nome válido!"	
		;;						
esac
