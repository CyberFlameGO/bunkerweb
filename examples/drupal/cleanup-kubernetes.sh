#!/bin/bash

if [ $(id -u) -ne 0 ] ; then
	echo "❌ Run me as root"
	exit 1
fi

helm delete drupal
kubectl delete pvc data-drupal-mariadb-0