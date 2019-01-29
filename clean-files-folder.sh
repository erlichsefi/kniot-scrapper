#!/bin/bash

cd ./files/

for i in * ; do
  if [ -d "$i" ]; then
   rm -f ./$i/*
  fi
done

