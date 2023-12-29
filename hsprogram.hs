import System.Environment

-- Color Flip Program From Haskell
flipColor :: [Int] -> [Int]
flipColor [] = []
flipColor (x : xs) = [255 - x] ++ flipColor xs

-- Main function
main :: IO ()
main = do
  args <- getArgs
  let numbers = map read args :: [Int]
      result = flipColor numbers
      resultStrings = map show result
      outputString = unwords resultStrings
  putStrLn outputString
