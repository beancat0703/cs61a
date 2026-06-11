(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1)
  ) 
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (repeat f n)
  (if (= n 0) (lambda (x) x)
    (composed (repeat f (- n 1)) f)
  )
)


(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (if (= (modulo (max a b) (min a b)) 0)
  (min a b)
  (gcd (modulo (max a b) (min a b)) (min a b)))
)

(define (exp b n)
  (define (helper n so-far) 
    (if (= n 0)
      so-far
      (helper (- n 1) (* b so-far))
    )
  )
  (helper n 1))

(define (swap s)
  (define (helper sofar rest)
    (cond
      ((null? rest) sofar)
      ((null? (cdr rest)) (append sofar rest))
      (else (helper (append sofar (list (car (cdr rest)) (car rest))) (cdr (cdr rest))))
    ))
  (helper () s)
)

(define (make-adder num) 'YOUR-CODE-HERE)
