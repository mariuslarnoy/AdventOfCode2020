module Main where

import System.IO
import Control.Monad

main :: IO()
main = do
    let list = []
    handle <- openFile "inputDay2.txt" ReadMode
    contents <- hGetContents handle
    let singlewords = words contents
        list = singlewords 
    print list
    hClose handle

f :: [String] -> [Int]
f = map read