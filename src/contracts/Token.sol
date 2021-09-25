pragma solidity^0.8.0;
//import "openzeppelin-solidity/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


contract Token {

	using SafeMath for uint;

	string public name = "Fritz Token";
	string public symbol = "Fritz";
	uint256 public decimals = 18;
	uint256 public totalSupply;

	// track balances
	//mapping = key value pairs (address and token balances)
	mapping(address => uint256) public balanceOf;


	// send tokens


	constructor() public {
		totalSupply = 1000000 * (10**decimals);
		balanceOf[msg.sender] = totalSupply;
	}
	
	function transfer(address _to, uint256 _value) public returns (bool success) {
		balanceOf[msg.sender] = balanceOf[msg.sender].sub(_value);
		balanceOf[_to] = balanceOf[_to].add(_value);
		return true;
	}
}

