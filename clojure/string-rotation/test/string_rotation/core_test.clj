(ns string-rotation.core-test
  (:require [clojure.test :refer :all]
            [string-rotation.core :refer :all]))

; (deftest a-test
;   (testing "FIXME, I fail."
;     (is (= 0 1))))

(deftest example-tests
  (are [s1 s2 answer] (= (shifted-diff s1 s2) answer)
    "hoop" "pooh" -1
    "coffee" "eecoff" 2
    "eecoff" "coffee" 4
    ))
