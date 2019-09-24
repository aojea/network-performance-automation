#! /bin/sh

set -eu

LINKERD2_VERSION=${LINKERD2_VERSION:-stable-2.5.0}

OS=$(uname -s)
arch=$(uname -m)
case $OS in
  CYGWIN*)
    OS=windows.exe
    ;;
  Darwin)
    ;;
  Linux)
    case $arch in
      x86_64)
        ;;
      *)
        echo "There is no linkerd $OS support for $arch" >&2
        exit 1
        ;;
    esac
    ;;
  *)
    echo "There is no linkerd support for $OS/$arch (yet...)" >&2
    exit 1
    ;;
esac
OS=$(echo $OS | tr [:upper:] [:lower:])

filename="linkerd2-cli-${LINKERD2_VERSION}-${OS}"
url="https://github.com/linkerd/linkerd2/releases/download/${LINKERD2_VERSION}/${filename}"

echo "Linkerd was successfully installed 🎉"
echo ""
echo "Add the linkerd CLI to your path with:"
echo ""
echo "  export PATH=\$PATH:\$HOME/.linkerd2/bin"
echo ""
echo "Now run:"
echo ""
echo "  linkerd check --pre                     # validate that Linkerd can be installed"
echo "  linkerd install | kubectl apply -f -    # install the control plane into the 'linkerd' namespace"
echo "  linkerd check                           # validate everything worked!"
echo "  linkerd dashboard                       # launch the dashboard"
echo ""
echo "Looking for more? Visit https://linkerd.io/2/next-steps"
echo ""
