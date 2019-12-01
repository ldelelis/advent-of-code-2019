module_fuel :: Int -> Int
module_fuel n = n `div` 3 - 2

fuel :: Int -> Int
fuel n
    | n < 9 = 0
    | otherwise = module_fuel n + fuel (module_fuel n)

main :: IO ()
main = do
    content <- getContents
    print . foldl (\x y -> x + fuel y) 0 . map read . lines $ content