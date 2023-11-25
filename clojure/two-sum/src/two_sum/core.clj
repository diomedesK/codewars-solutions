(ns two-sum.core)

; (defn twosum 
;   [ numbers target ]
;   ( dorun ( map-indexed 
;      (fn [i item_i]

;        ( dorun ( map-indexed 
;                  ( fn [j item_j]
;                    ( if (= (+ item_i item_j) target )
;                      (println item_i  item_j "(" target ")") ;; return [i, j] instead
;                      )

;                   )
;                  (subvec numbers (+ i 1) (count numbers) )
;                  ))

;        )
;      numbers
;      ))
;   [0 0]
;   )

(defn twosum 
  [numbers target]
  (let [result (for [i (range (count numbers)) 
                 j (range (inc i) (count numbers))
                 :when (= (+ (numbers i) (numbers j)) target )]
                 [i j])]
    (if (empty? result)
      [0 0]
      (first result)
      )
    )
)


; (defn twosum
;   [numbers target]
;   (let [result (for [i (range (count numbers))
;                      j (range (inc i) (count numbers))
;                      :when (= (+ (numbers i) (numbers j)) target)]
;                   [i j])]
;     (if (empty? result)
;       [0 0] ; Return [0 0] if no pairs are found
;       (first result))))
