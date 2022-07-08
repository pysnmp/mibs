#
# PySNMP MIB module OPENBSD-SNMPD-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SNMPD-CONF
# Produced by pysmi-1.1.8 at Fri Jul  8 08:25:56 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
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
ObjectIdentity, Integer32, Bits, MibIdentifier, iso, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, IpAddress, ModuleIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Bits", "MibIdentifier", "iso", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "IpAddress", "ModuleIdentity", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
