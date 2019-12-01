fuel :: Int -> Int
fuel 0 = 0
fuel n = n `div` 3 - 2

main :: IO ()
main = do
    content <- getContents
    print . foldl (\x y -> x + fuel y) 0 . map read . lines $ content
