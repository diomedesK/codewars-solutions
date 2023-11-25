(ns string-rotation.core)

;; this is my first day ever studying clojure, pls forgive me 

( defn shifted-diff 
  [w1 w2]
  ( if (= w1 w2)
    0 
   ( loop [x 0] 
     ( if (< x (count w1))
       ( let [shifted-word (subs (str w1 w1) x (+ x (count w1) ) )]
         ( if (= shifted-word w2) 
           (- (count w1) x)
           (recur (+ x 1))
           )
         )
       -1

      ) 

     ) ;; end loop

   ) ;; endif

  )


; (defn shifted-diff 
;   [word1 word2] 
;   ( let [ newstr (str word1 "" word1) ]

;     ( let
;      [ res
;       (map (fn [num]  (if (= (str (subs newstr num (+ num ( count word1 )) ) ) word2) (- (count word1) num) ) ) ( range 0 (count word1) ))
;       ]

;      ( let [ r (if (= word1 word2) 0 ( first ( remove nil? res ) ) ) ]
;        (if (not= r nil ) r -1)
;        )

;      )
;   )

; )

