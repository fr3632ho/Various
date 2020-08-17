main = do
  input1 <- getLine
  let n = (read input1 :: Int)
  let val = (getStatues n 0)
  putStrLn (show val)


getStatues :: Int -> Int -> Int
getStatues n x
  | 2^x < n = getStatues n (x + 1)
  | otherwise = x + 1
