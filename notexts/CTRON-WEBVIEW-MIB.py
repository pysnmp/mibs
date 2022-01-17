#
# PySNMP MIB module CTRON-WEBVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WEBVIEW-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 14:56:42 2022
# On host fv-az127-428 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctApplication, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctApplication")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Gauge32, NotificationType, Integer32, IpAddress, Counter64, Unsigned32, ObjectIdentity, Counter32, TimeTicks, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "IpAddress", "Counter64", "Unsigned32", "ObjectIdentity", "Counter32", "TimeTicks", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctWebView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4))
ctEwvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1))
ctEwvStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 2))
ctEwvDocSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1))
ctEwvDocSupportAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdmin.setStatus('mandatory')
ctEwvDocSupportLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportLocation.setStatus('mandatory')
ctEwvDocSupportAdminUID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdminUID.setStatus('mandatory')
ctEwvDocSupportUsername = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportUsername.setStatus('mandatory')
ctEwvDocSupportPassword = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportPassword.setStatus('mandatory')
ctEwvSystemParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2))
ctEwvAuthScheme = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("basic", 2), ("digest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthScheme.setStatus('mandatory')
ctEwvAuthNonceValidCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthNonceValidCount.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WEBVIEW-MIB", ctEwvDocSupportLocation=ctEwvDocSupportLocation, ctWebView=ctWebView, ctEwvStatus=ctEwvStatus, ctEwvAuthNonceValidCount=ctEwvAuthNonceValidCount, ctEwvDocSupportAdmin=ctEwvDocSupportAdmin, ctEwvDocSupportUsername=ctEwvDocSupportUsername, ctEwvConfiguration=ctEwvConfiguration, ctEwvDocSupportAdminUID=ctEwvDocSupportAdminUID, ctEwvAuthScheme=ctEwvAuthScheme, ctEwvDocSupportPassword=ctEwvDocSupportPassword, ctEwvDocSupport=ctEwvDocSupport, ctEwvSystemParameters=ctEwvSystemParameters)
