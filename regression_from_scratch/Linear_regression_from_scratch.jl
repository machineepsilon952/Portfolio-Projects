function norm(v::Array)
    return sqrt(v'*v)
end

function qr(Q)
    dim=size(Q)
    R=zeros(dim[1],dim[2])

    for k=1:dim[2]
        for L=1:k-1
            R[L,k]=Q[:,L]'*Q[:,k] 
            Q[:,k]=Q[:,k]-R[L,k]*Q[:,L]
        end
        R[k,k]=norm(Q[:,k])
        Q[:,k]=Q[:,k]/R[k,k]
    end
    return Q,R;


end

function backsub(A::Array,b::Array)
    n = size(b)[1]
    x = zeros(n)
    x[n] = b[n]/A[n,n]
    for i = (n-1):-1:1
        x[i] = (b[i] - A[i,i+1:n]'*x[i+1:n])/A[i,i]
    end
    return x 
end

function qrls(A::Array, b::Array)
    Q, R = qr(A)
    b = Q'*b
    x =backsub(R::Array, b::Array)
    return x
    
end

function evaluate_ls(data, x) # assumes that we are always fitting an intercept using column 1 of the origional matrix a
    x[1]+x[2:length(x)]'*data
end








