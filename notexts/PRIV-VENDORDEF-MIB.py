#
# PySNMP MIB module PRIV-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:56:07 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, enterprises, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Gauge32, Bits, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "enterprises", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
privateVendorOID = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
privateVendorOID.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: privateVendorOID.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: privateVendorOID.setOrganization('BATM Advanced Communication')
mibBuilder.exportSymbols("PRIV-VENDORDEF-MIB", PYSNMP_MODULE_ID=privateVendorOID, privateVendorOID=privateVendorOID)
