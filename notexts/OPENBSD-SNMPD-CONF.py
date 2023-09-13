#
# PySNMP MIB module OPENBSD-SNMPD-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SNMPD-CONF
# Produced by pysmi-1.1.8 at Wed Sep 13 15:00:38 2023
# On host fv-az629-233 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
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
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpMIB, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpMIB")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter32, Counter64, Integer32, ModuleIdentity, NotificationType, TimeTicks, Bits, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "TimeTicks", "Bits", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
