#
# PySNMP MIB module OPENBSD-SNMPD-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SNMPD-CONF
# Produced by pysmi-1.1.12 at Wed May 29 10:59:17 2024
# On host fv-az1200-312 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
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
Bits, Counter64, NotificationType, Integer32, Unsigned32, IpAddress, iso, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "iso", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
