#
# PySNMP MIB module OPENBSD-SNMPD-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SNMPD-CONF
# Produced by pysmi-1.1.8 at Thu Apr 27 10:41:30 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dot1dBridge, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBridge")
hostResourcesMibModule, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hostResourcesMibModule")
ianaifType, = mibBuilder.importSymbols("IANAifType-MIB", "ianaifType")
ifMIB, = mibBuilder.importSymbols("IF-MIB", "ifMIB")
inetAddressMIB, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "inetAddressMIB")
ipForward, = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipForward")
ipMIB, = mibBuilder.importSymbols("IP-MIB", "ipMIB")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
carpMIBObjects, = mibBuilder.importSymbols("OPENBSD-CARP-MIB", "carpMIBObjects")
memMIBObjects, = mibBuilder.importSymbols("OPENBSD-MEM-MIB", "memMIBObjects")
pfMIBObjects, = mibBuilder.importSymbols("OPENBSD-PF-MIB", "pfMIBObjects")
sensorsMIBObjects, = mibBuilder.importSymbols("OPENBSD-SENSORS-MIB", "sensorsMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmpMIB, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpMIB")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter64, iso, NotificationType, Unsigned32, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter64", "iso", "NotificationType", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
