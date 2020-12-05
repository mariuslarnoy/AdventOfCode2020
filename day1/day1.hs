module Main where

import System.IO
import Control.Monad

fst1 :: (Int,Int,Int) -> Int
fst1 (x,y,z) = x

snd1 :: (Int,Int,Int) -> Int
snd1 (x,y,z) = y

third :: (Int,Int,Int) -> Int
third (x,y,z) = z

solve :: [Int] -> Int
solve xs = fst1 (head res) * snd1 (head res) * third (head res)
    where
       res = [(x,y,z) | x <- xs, y <- xs, z <- xs, x + y + z == 2020]

main :: IO()
main = do
    let list = []
    handle <- openFile "inputDay1.txt" ReadMode
    contents <- hGetContents handle
    let singlewords = words contents
        list = f singlewords 
    print (solve list)
    hClose handle

f :: [String] -> [Int]
f = map read